# MI-030 — Multiquadratic packaging turns source cost into discriminant complexity

**Evidence level:** exact endpoint/source-cost deduction plus classical conductor--discriminant and effective Chebotarev input from [MC-303](../../findings/MC-303-multiquadratic-discriminant-chebotarev-range-barrier.md)

The selected quadratic source modes can be packaged into one object rather than controlled character by character. If `lambda_1,...,lambda_R` are independent endpoint shell functionals and `chi_1,...,chi_R` are source-cost-minimizing quadratic representatives, shell independence forces the global characters to be independent. Their compositum is therefore a multiquadratic field `K/Q` with

`[K:Q]=2^R`.

For every subset mode `I`, the primitive conductor `f_I` is itself a lower-prime representative of `lambda_I`, so `f_I>=Q(lambda_I)`. The conductor--discriminant formula then converts the whole source-cost spectrum into

`|D_K| = prod_I f_I`.

Under the endpoint-partition hypothesis used by MC-296, all but a central-binomial fraction of the subset modes have source cost above the Page threshold `D_y`. Hence

`log |D_K| > H_R log D_y`, with `H_R/2^R = 1-O(R^-1/2)`.

At the blind-support floor `R~log_2 log y`, this gives

`log |D_K| >= (log y)^(2-o(1))/log log y`.

So the exact reorganization into Frobenius classes does not make the mixing problem cheap. Standard effective Chebotarev pays for the same endpoint complexity through `D_K` and `[K:Q]`: even after dropping exceptional-zero costs, the classical range contains a term `(log D_K)^2/[K:Q]` of size at least `(log y)^(3-o(1))/(log log y)^2`, already much larger than the shell-scale budget `log y`. The improved black-box range also fails because `D_K` is superpolynomial in `y` on the logarithmic scale.

This is not evidence that the actual Frobenius classes fail to mix at scale `y`. It is a **complexity-transfer obstruction**: the source modes that were too expensive for generic large-sieve capacity reappear as discriminant complexity when compressed into one multiquadratic field. A successful collective theorem must exploit structure not summarized by the generic pair `([K:Q],D_K)`—for example the special ramification/character geometry of this selected family, a family-specific zero-density theorem, or another source-coupled relation among the modes.

The reusable distinction is therefore between **packaging** and **compression**. Combining many source coordinates into one algebraic object is only useful if the theorem acting on that object does not charge essentially the same source complexity through a different invariant.
