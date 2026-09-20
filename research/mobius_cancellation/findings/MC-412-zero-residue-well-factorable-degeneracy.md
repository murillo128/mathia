# MC-412 — Divisor-incidence well-factorability sits in the degenerate zero-residue sector

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the well-factorable upper-sieve branch of `MC-409`--`MC-411`. Let `chi` be a primitive Dirichlet character of conductor `q`, let `lambda_d` be any finitely supported coefficient sequence, and define

\[
w(n):=\sum_{d\mid n}\lambda_d,
\qquad
S_\chi(N;\lambda):=\sum_{n\le N}w(n)\chi(n).
\tag{1}
\]

The divisor variable can formally be written as a progression modulus,

\[
S_\chi(N;\lambda)
=
\sum_d\lambda_d
\sum_{\substack{n\le N\\ n\equiv0\pmod d}}\chi(n),
\tag{2}
\]

but this is exactly the **degenerate zero-residue class**. It does not place the well-factorable variable in the arithmetic role used by Bombieri--Friedlander--Iwaniec/Maynard/Pascadi/Yang distribution theorems.

Indeed, if `(d,q)>1`, every term in the inner sum of `(2)` vanishes. If `(d,q)=1`, writing `n=dm` gives the exact identity

\[
\boxed{
\sum_{\substack{n\le N\\ n\equiv0\pmod d}}\chi(n)
=
\chi(d)M_\chi(N/d),
\qquad
M_\chi(X):=\sum_{m\le X}\chi(m).
}
\tag{3}
\]

Thus

\[
\boxed{
S_\chi(N;\lambda)
=
\sum_{\substack{d\\(d,q)=1}}
\lambda_d\chi(d)M_\chi(N/d).
}
\tag{4}
\]

The only modular relation supplied intrinsically by the sieve coefficient is therefore `n=0 (mod d)`, and that relation disappears completely under the change of variables `n=dm`. Factorability of `lambda_d` can organize the coefficient side of `(4)`, but it does not by itself create a reduced residue, reciprocal phase, or comparison between independently varying products.

This gives a precise prior-art boundary for the current branch. Modern well-factorable distribution theorems gain strength when the factorable variable is the **modulus of a nonzero reduced congruence**, schematically

\[
lp\equiv a\pmod d,
\qquad a\ne0,
\tag{5}
\]

and dispersion/completion turns that relation into genuinely nonseparable reciprocal/Kloosterman-type phases. The recent convolution theorem of Zhiyuan Yang (2026), for example, keeps a fixed nonzero residue `a`, averages with a well-factorable modulus weight, and in the proof reaches phases containing a reciprocal variable multiplied by `a`. The nonzero residue is not cosmetic: setting the intrinsic divisor relation to `a=0` removes exactly the affine displacement that prevents the scalarization `(3)`.

Equivalently, resolving the source character into residue classes modulo `q` does not repair the mismatch. For a unit source residue `a (mod q)` and `(d,q)=1`, the simultaneous conditions

\[
n\equiv a\pmod q,
\qquad d\mid n
\tag{6}
\]

become, after `n=dm`,

\[
m\equiv a\overline d\pmod q.
\tag{7}
\]

So `d` merely **permutes residues inside the fixed source modulus `q`**. It still does not become the varying progression modulus over which well-factorable Bombieri--Vinogradov theorems average. This is the residue-class counterpart of the dual-mode permutation proved in `MC-411`.

Consequently, the surviving `MC-409` route is narrower than “apply a well-factorable distribution theorem.” A useful argument must first generate a nonzero affine/congruence/reciprocal relation in which the sieve factors cannot be removed by `n=dm` or by the residue permutation `(7)`. Only after that step can the classical well-factorable dispersion machinery plausibly act on the same variable.

No character-sum improvement and no estimate for `M(x)` follows.

## 1. The divisor progression is algebraically trivial for a fixed multiplicative character

Starting from `(1)` and exchanging finite sums gives `(2)`. For a primitive character modulo `q`, `chi(n)=0` when `(n,q)>1`. Hence if `(d,q)>1`, every multiple of `d` contributes zero.

When `(d,q)=1`, every integer in the inner sum is uniquely `n=dm`, and complete multiplicativity gives

\[
\chi(dm)=\chi(d)\chi(m).
\tag{8}
\]

This proves `(3)` and `(4)` exactly. No estimate, completion, or analytic continuation is involved.

The point is representational. Writing `d|n` as `n=0 (mod d)` makes the expression look superficially like a progression problem, but the zero class carries no transverse arithmetic information: it is simply the multiplication map `m -> dm`. For a fixed multiplicative character that map is diagonalized by `chi` itself.

This also shows why generic coefficient factorization did not help in `MC-410`. If `lambda=alpha*beta`, then substituting `(4)` and expanding the convolution merely produces the separable product `chi(u)chi(v)chi(m)`. The apparently different “progression-modulus” interpretation has added no structure.

## 2. A fixed source residue turns the divisor into a permutation, not a modulus average

One can instead expand the source character through its values on the reduced residue classes modulo `q`. For each unit residue `a`, consider the contribution with `n=a (mod q)` together with the divisor condition `d|n`.

For `(d,q)=1`, the Chinese remainder theorem and the substitution `n=dm` give exactly `(7)`. Multiplication by `d^{-1}` is a permutation of `(Z/qZ)^*`. Therefore the family of source residues is merely relabeled as `d` varies.

This exposes two distinct averaging axes:

- the source problem keeps the conductor `q` fixed and Fourier-analyzes or permutes residues modulo `q`;
- classical well-factorable Bombieri--Vinogradov results keep a reduced residue fixed and average the **modulus** against a well-factorable sequence.

The divisor identity does not transpose one axis into the other. Any attempted transplant must exhibit an additional identity that genuinely puts `d` into a nontrivial modulus relation, rather than merely changing coordinates on the fixed source residue group.

## 3. Why the successful well-factorable prior art is structurally different

Yang, *Convolution-type Bombieri-Vinogradov theorem with well-factorable Weights, and its applications* (arXiv:2608.13299, 13 August 2026), studies sums of the form

\[
\sum_d\sum_r\gamma_d\lambda_r
\left(
\sum_{lp\equiv a\pmod{dr}}1
-
\frac1{\varphi(dr)}\sum_{(lp,dr)=1}1
\right),
\tag{9}
\]

with a fixed nonzero residue `a` and a well-factorable modulus weight. The paper extends the Bombieri--Friedlander--Iwaniec/Maynard/Pascadi line and explicitly uses incomplete Kloosterman/exceptional-large-sieve input.

The proof displays the structural feature relevant here. After dispersion and truncated Poisson summation, Yang reaches reciprocal phases schematically containing

\[
e\!\left(
 a h k\frac{\overline{n_2q_1}}{n_1q_2}
\right),
\tag{10}
\]

with independently varying modulus factors. The affine datum `a` survives completion and prevents the factorable variables from being absorbed by a single multiplicative reindexing. This is precisely the kind of nonseparable arithmetic geometry that is absent from `(2)`--`(4)`.

Maynard's earlier well-factorable theorem and Pascadi's later triply-well-factorable improvements live on the same progression-distribution side of this boundary: the factorable weight is attached to a genuine progression modulus, not merely to a divisor of the summation variable.

The comparison does **not** assert that nonzero residue alone is sufficient for a useful estimate, nor that Yang's theorem can be applied to the Mathia source after a formal rewrite. It identifies the exact structural datum present in the successful prior art and absent from the current fixed-character form.

## 4. Prior-art and novelty boundary

The identities `(2)`--`(4)` and `(6)`--`(8)` are elementary divisor algebra, complete multiplicativity, and the Chinese remainder theorem. No novelty is claimed for them.

Well-factorable distribution of primes in reduced arithmetic progressions is established classical prior art, from Bombieri--Friedlander--Iwaniec through Maynard and the recent Pascadi extensions. Yang's 2026 convolution theorem is a particularly close current reference because it makes both ingredients visible in one statement: the factorable sequence weights the progression modulus, while the residue `a` is fixed and nonzero. Its proof then produces the reciprocal phase in `(10)` only after that congruence structure is present.

A targeted literature audit on 20 September 2026 found no theorem that turns the zero-residue divisor identity `(2)` for a fixed Dirichlet character into a comparable well-factorable modulus average without adding another arithmetic relation. No novelty claim is made from that absence.

The durable Mathia contribution is the **frontier classification**: `MC-409` supplied a coefficient with genuine linear-sieve factorability, but the same variable enters the source-character sum only through the degenerate congruence `n=0 (mod d)`. `MC-410` and `MC-411` showed analytically that this remains separable under Mellin and ordinary Fourier completion; the present finding explains the mismatch directly in the language of the successful well-factorable progression literature.

## Boundaries and falsification tests

- **This is not a no-go theorem for upper-sieve weights.** Their positivity, small total mass, support restrictions, and special Rosser--Iwaniec structure may still matter. The finding rules out crediting *divisor incidence itself* as the nontrivial progression geometry.
- **A shifted divisor relation is outside the obstruction.** Conditions such as `d|(n-a)` with `a != 0`, translated character phases `chi(dm+a)`, or congruences comparing two independently varying products can survive the substitution `n=dm` and remain live.
- **A reciprocal/Kloosterman phase generated by another identity is outside the obstruction.** Once such a phase exists, well-factorability may become useful exactly as in the distribution literature.
- **The fixed source modulus may still support other family estimates.** The statement only says that varying `d` through the divisor weight does not automatically provide the modulus-average axis of Bombieri--Vinogradov theory.
- **Imprimitive presentations add zero masks, not a free affine displacement.** Any claimed gain from a larger presentation modulus must identify arithmetic information surviving conductor descent rather than treating the mask as new oscillation.
- **No use of RH or zero-free continuation.** The exact reduction is finite and algebraic.

## Consequence for the research line

The immediate “well-factorable coefficient -> well-factorable Bombieri--Vinogradov theorem” transplant is now classified as structurally invalid for the fixed source-character form. The coefficient is genuinely well-factorable, but it occupies the wrong slot: it describes the zero-residue divisor condition instead of a nonzero reduced progression modulus.

The next useful calculation should therefore start **before** applying absolute values or scalarizing `chi(dm)`, and ask whether the actual source/sieve identity can produce a shifted congruence, a comparison of two products, or a reciprocal phase. If it cannot, further optimization of the factorization `lambda=alpha*beta` remains on the separable side of the barrier already exposed by `MC-410`--`MC-411`.