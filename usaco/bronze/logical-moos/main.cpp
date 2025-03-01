#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

// Precompute factorials and inverses up to 2000 (or a bit more).
// We'll use these for nPk, nCk, etc., modulo 1e9+7.
static const int MAXN = 200000; // large enough for safety
long long fact[MAXN+1], invFact[MAXN+1];

// Fast exponentiation
long long modExp(long long base, int exp) {
    long long result = 1 % MOD;
    while(exp > 0) {
        if(exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

// Compute inverses and factorials
void initFactorials(int n) {
    fact[0] = 1;
    for(int i=1; i<=n; i++){
        fact[i] = fact[i-1] * i % MOD;
    }
    invFact[n] = modExp(fact[n], MOD-2); // Fermat's little theorem for inverse
    for(int i=n-1; i>=0; i--){
        invFact[i] = (invFact[i+1] * (i+1)) % MOD;
    }
}

// nCk
long long nCk(int n, int k){
    if(k<0 || k>n) return 0;
    return fact[n]*invFact[k]%MOD*invFact[n-k]%MOD;
}

// We will store constraints p[i] = j in arrays: fixedPos[i] = j, or -1 if none.
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Initialize factorial tables once (up to 2000 is enough).
    initFactorials(2000);

    int T, N;
    cin >> T >> N;
    // We handle T test cases, each with K constraints of the form p_i = j.

    // Precompute D = floor(N/2).
    int D = N/2;  // works for both even & odd N

    // -----------------------
    // Identify the "low set" and "high set" of values.
    // For even N = 2D, low set = {0,1,...,D-1}, high set = {D,D+1,...,2D-1}.
    // For odd N = 2D+1, we can choose low set = {0,1,...,D}, high set = {D+1,...,2D} (size D and D+1, or vice versa).
    // We'll define them consistently as:
    //   lowSet = the first ceil(N/2) values,
    //   highSet = the last floor(N/2) values.
    // Then we'll consider 2 patterns of interleaving: (L->H->L->H->...) or (H->L->H->L->...).

    // Number of elements in lowSet:
    int sizeLow = (N+1)/2;      // ceil(N/2)
    int sizeHigh = N/2;         // floor(N/2)
    // The actual values in each set are:
    //   lowSet = [0,1,2,...,sizeLow-1]
    //   highSet= [sizeLow, sizeLow+1, ..., N-1]
    // We'll keep them in ascending order for convenience.

    // For each test case, we read K constraints, then handle them.
    // We will do:
    //   - Build an array fixedPos[] of length N, each init to -1 meaning "no constraint for that position".
    //   - Also track which position (if any) each value is forced into: forcedValPos[value] = position or -1.
    // If there's a conflict => answer=0 immediately.

    while(T--){
        int K; cin >> K;
        vector<int> fixedPos(N, -1);      // fixedPos[i] = which value is forced at p[i], or -1
        vector<int> forcedValPos(N, -1);  // forcedValPos[val] = which index i is forced, or -1
        bool conflict = false;
        for(int _=0; _<K; _++){
            int i, j;
            cin >> i >> j;
            if(fixedPos[i] != -1 && fixedPos[i] != j){
                // Two constraints conflict at same position
                conflict = true;
            }
            if(forcedValPos[j] != -1 && forcedValPos[j] != i){
                // Two constraints want same value j in different positions
                conflict = true;
            }
            fixedPos[i] = j;
            forcedValPos[j] = i;
        }
        if(conflict){
            // No permutations possible
            cout << 0 << "\n";
            continue;
        }

        // We'll count how many ways for Pattern A (start with lowSet) plus Pattern B (start with highSet).

        // --- Function to count valid ways for a specific pattern of L/H blocks. ---
        // pattern[] will be an array of length N whose entries are 'L' or 'H',
        // telling whether position k uses an element from lowSet or from highSet.
        // For example, if we do L,H,L,H,... for N=5 => pattern = [L,H,L,H,L].
        // Then we must assign exactly 'sizeLow' distinct values from lowSet to those L positions
        // in *strictly increasing* order of the *indices in lowSet*,
        // subject to the fixedPos[] constraints.
        // Similarly for H positions.

        auto countPattern = [&](const vector<char> &pattern)->long long {
            // Collect the positions that require L, and the positions that require H.
            // Then we see if any fixedPos in those positions is a value not in that half => conflict => 0.
            // Next, among the L positions, we see which subset of the lowSet are forced by constraints.
            // We'll end up with "some positions are forced to certain L-values", "some L-values are forced to certain positions," etc.
            // Then the leftover L-positions can be filled with leftover L-values in any order that respects
            // the "strict ascending order of the indices from the lowSet".  But effectively, that just means
            // we do a 1-to-1 matching between the set of free L-positions and free L-values.  The count is just the factorial of
            // (number of free positions in L) if everything is consistent, because we must place them in ascending order of the lowSet’s index.
            //
            // Implementation approach:
            //   1) Let Lpos = all indices k s.t. pattern[k] = 'L'.  Let #Lpos = sizeLow.
            //   2) For each forced position k in Lpos with forced value v, check if v < sizeLow. If not, conflict => return 0.
            //      Also check if that v is not used yet. If used => conflict => 0.  Then fix that pairing.
            //   3) Count how many L-values remain unforced (call that Rl) and how many L-positions remain unforced (also Rl).
            //      We can assign those Rl leftover values to Rl leftover positions in Rl! ways (mod M).
            //   4) Repeat similarly for the H half.
            //   5) Multiply the two results (mod M) and return.

            // Gather positions for L and H
            vector<int> Lpos, Hpos;
            for(int i=0; i<N; i++){
                if(pattern[i] == 'L') Lpos.push_back(i);
                else Hpos.push_back(i);
            }
            // sanity check
            if((int)Lpos.size() != sizeLow || (int)Hpos.size() != sizeHigh){
                return 0LL; // shouldn't happen
            }

            // Track used values in L and H
            vector<bool> usedLow(sizeLow,false), usedHigh(sizeHigh,false);

            // Check constraints in Lpos
            int freeL = sizeLow; // how many L-values are still free
            for(int p: Lpos){
                int val = fixedPos[p];
                if(val == -1) continue; // no constraint
                // constraint says p-th position has value = val
                if(val < 0 || val >= N) return 0LL; // bad but shouldn't happen
                if(val >= sizeLow) {
                    // forced a value that belongs to the "high" set into an "L" slot => conflict
                    return 0LL;
                }
                // see if that low-value is already used
                if(usedLow[val]) {
                    return 0LL; // conflict
                }
                usedLow[val] = true;
                freeL--;
            }

            // Now among the "low set" = {0..sizeLow-1}, some might be forced to positions in Lpos
            // also check if forcedValPos for those "low" values is consistent
            for(int lv=0; lv<sizeLow; lv++){
                int forcedPosIndex = forcedValPos[lv];
                if(forcedPosIndex != -1){
                    // must be in Lpos
                    if(pattern[forcedPosIndex] != 'L'){
                        return 0LL;
                    }
                }
            }

            // The unforced L-values can go to unforced L-positions in ANY permutation? 
            // Actually, to keep consecutive differences >= floor(N/2), we must place them in the order of ascending "lv".
            // But once we fix which L-position gets lv, the actual numeric difference is determined.  
            // For counting purposes, *as soon as we haven't forced a specific lv into a specific position*, 
            // we are free to choose among any of the leftover L-positions.  
            // The number of ways is simply freeL! (because we are matching leftover L-values to leftover L-positions one-to-one).

            long long waysL = 1;
            waysL = (waysL * fact[freeL]) % MOD;

            // Similarly for Hpos
            int freeH = sizeHigh;
            for(int p: Hpos){
                int val = fixedPos[p];
                if(val == -1) continue;
                if(val < sizeLow) {
                    // forced a "low" value in an "H" slot => conflict
                    return 0LL;
                }
                int hv = val - sizeLow;
                if(hv < 0 || hv >= sizeHigh) {
                    return 0LL; // out of range
                }
                if(usedHigh[hv]) {
                    return 0LL; // conflict
                }
                usedHigh[hv] = true;
                freeH--;
            }
            // check forcedValPos for those in the high set
            for(int hv=0; hv<sizeHigh; hv++){
                int actualVal = hv + sizeLow; 
                int fPos = forcedValPos[actualVal];
                if(fPos != -1){
                    // must be in Hpos
                    if(pattern[fPos] != 'H') {
                        return 0LL;
                    }
                }
            }
            long long waysH = fact[freeH] % MOD;

            // total ways
            long long ans = (waysL * waysH) % MOD;
            return ans;
        };

        // Build the two possible patterns of length N:
        //   patternA: L,H,L,H,...   (if #L >= #H, we do L first, else H first)
        //   patternB: H,L,H,L,...
        // Actually, if N is odd, one pattern will have the extra L at the end, the other pattern will have the extra L at the beginning, etc.
        // We'll just systematically fill them:

        vector<char> patternA(N), patternB(N);

        // Let's define a small helper: 
        // If sizeLow == sizeHigh or sizeLow == sizeHigh+1, we do:
        //   patternA: L,H,L,H,... (the leftover L if odd)
        //   patternB: H,L,H,L,... (the leftover L if odd)
        // Because sizeLow >= sizeHigh always if we define low = ceil(N/2).
        // Then fill them accordingly.

        {
            // patternA: start with L
            for(int i=0; i<N; i++){
                if(i % 2 == 0) patternA[i] = 'L';
                else patternA[i] = 'H';
            }
            // patternB: start with H
            for(int i=0; i<N; i++){
                if(i % 2 == 0) patternB[i] = 'H';
                else patternB[i] = 'L';
            }
        }

        // Now count how many ways for each pattern
        long long waysA = countPattern(patternA);
        long long waysB = countPattern(patternB);

        long long ans = (waysA + waysB) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
