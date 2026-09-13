# MI-002 — Odd repeated-prime channels can be reembedded recursively; the dyadic channel is the scale-critical exception

**Evidence level:** exact inside the false-RH frontier construction of FD-088--FD-091. The square stripping and four-adic reembedding are exact up to a universal Jordan-weight condition number; the resulting lower mask has the full frontier exponent, not a proved fixed occupation fraction.

After the first canonical prime deflation, every selected row in the `p`-channel is still divisible by `p`. For odd `p`, strip that second copy and reembed `s=pt` as `4t` at

`C_p = 4 floor(A_p/p) = 4H/p^2 + O(1)`.

Floor quotients compose exactly, so the quotient-shell amplitude is unchanged. Jordan weights change by at most the universal factor `zeta(2)`, and every new row is divisible by `4`, hence lies in the nonsquarefree sector. For every odd `p>=3`, `C_p <= (4/9+o(1))H`, so the operation restores the missing eligibility at a genuinely lower physical scale.

The same mechanism is **exactly scale-critical at `p=2`**. Stripping `2^2` and multiplying by the smallest universal square that guarantees nonsquarefreeness gives `4 floor(A_2/2)=H+O(1)`: the scale gain disappears. The recursive-eligibility failure left by FD-090 is therefore not symmetric across the prime packet; after FD-091 it is concentrated in the dyadic channel plus one quantitative issue in the odd branch.

There is also a normalization gain. Pricing the odd reembedded state at `C_p^(2 sigma)` changes the carrier weight from `p^(-2 sigma)` to `p^(-4 sigma)`, so the predecessor family is summable already for `sigma>1/4`. At the RH-critical normalization `sigma=1/2`, no logarithmic predecessor entropy remains. Under the false-RH frontier hypothesis an odd channel therefore carries a nonsquarefree mask of full frontier exponent at the lower scale.

What is still missing is **iterability at fixed strength**. Full exponent does not imply `U_C >= c E_C`; the mask fraction may decay subpolynomially. A recursive contradiction must either upgrade the odd branch to a fixed occupation fraction/composition law or control the dyadic terminal channel where universal square reembedding consumes the entire contraction.

**Boundary.** This intuition is conditional on the false-RH frontier packet already constructed in the line. It does not prove a lower-state fixed occupation fraction, an infinite descent, or RH.