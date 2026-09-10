# MI-015 — Sign-support covariance gives a conditioned quadratic bridge but leaves one source-hard aggregate

**Evidence level:** exact mixed-covariance decoder, squarefree progression control, and affine-centering classification through MC-202

## Core intuition

Retaining the squarefree support field together with Möbius sign creates a genuinely cheaper algebraic route to the rough principal mode than the cubic residue statistics previously tested. The principal sum can be decoded from one uncentered mixed sign-support aggregate and one centered covariance, and the decoder is polynomially well-conditioned at logarithmic primorial scale.

The gain is real but stops at a sharp source boundary: the centered covariance is already harmless at the RH scale, so the whole unresolved burden is one uncentered same-residue mixed correlation. Affine centering cannot remove that burden without removing the principal coordinate itself.

## Strongest justified principle

MC-200 derives the exact identity `E_{1,2}-C_{1,2}=S(Q/phi-1)`, where `C_{1,2}` uses only centered nonprincipal sign/support sectors and `E_{1,2}` is the uncentered same-residue source aggregate. At `q=prod_{p<=c log X} p`, the denominator satisfies `Q/phi-1 >= X^(1-c-o(1))`, so this is not an ill-conditioned formal inversion.

MC-201 uses uniform squarefree progression counting to show that, for sufficiently small fixed `c`, the decoded contribution of `C_{1,2}` is already below the `X^(1/2+epsilon)` target scale. Thus the quadratic architecture genuinely narrows the source theorem to control of `E_{1,2}` alone.

MC-202 classifies the natural attempt to center the support factor inside that aggregate. Every affine centering splits exactly into a principal coefficient times `S` plus a transverse centered term. At the unique centering that cancels the principal coefficient, the decoder becomes singular and only the already-controlled covariance remains. Approximate cancellation weakens recoverability by precisely the same coefficient it suppresses.

## Program consequence

Attack `E_{1,2}` as the canonical remaining source object. Rewrite it through fixed-shift, factorization, sieve, or multiscale structure and ask whether the required estimate is strictly cheaper than a Mertens bound after division by `Q/phi-1`. Preserve the uncentered principal-sensitive degree of freedom until that source theorem has been applied.

Do not spend effort tuning affine centering constants: the exact decomposition shows that normalization cannot improve the information/conditioning tradeoff by itself.

## Counterevidence / boundary

The decoder does not prove a new Möbius cancellation estimate. `E_{1,2}` may be as hard as the original principal sum, and fixed-shift decorrelation currently provides no obvious power budget at the required growing-modulus geometry. Other support-sensitive observables or several coupled scales could produce a different source identity.

The small-primorial covariance estimate depends on choosing `c` sufficiently small relative to the target epsilon; it is a target-scale simplification, not a uniform statement for all primorial growth.

## Epistemic status

**Exact positive algebraic narrowing: sign plus squarefree support yields a well-conditioned quadratic decoder whose transverse covariance is RH-scale harmless, leaving one explicit uncentered mixed source aggregate as the load-bearing arithmetic theorem; affine centering cannot remove that theorem for free.**

## Falsification criterion

Show that the MC-200 decoder becomes target-scale ill-conditioned in the admitted logarithmic-primorial regime, invalidate the MC-201 covariance bound under its hypotheses, or derive an affine centering whose principal coefficient vanishes while a well-conditioned independent route to `S` survives without additional source information.
