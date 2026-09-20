# MC-409 — Well-factorable upper sieve preserves the prime-frame architecture

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `CANDIDATE-NEW-STRUCTURE` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The squared Selberg majorant used in `MC-377`--`MC-404` is **not forced by the Bombieri/Hilbert-space prime-frame architecture**. It can be replaced, at the representation level, by a nonnegative upper-bound linear-sieve weight whose coefficient sequence is a finite linear combination of well-factorable sequences.

Let `P(z)` be the product of the chosen sifting primes below `z`, and let `(lambda_d^+)` be a well-factorable variant of the upper-bound linear-sieve coefficients of level `D`, normalized by `lambda_1^+=1` and supported on squarefree `d<=D`, `d|P(z)`. Put

\[
w(n):=\sum_{d\mid n}\lambda_d^+.
\tag{1}
\]

Then the defining upper-bound-sieve inequality gives

\[
\boxed{
w(n)\ge \mathbf 1_{(n,P(z))=1}\ge0.
}
\tag{2}
\]

In particular, if a shell prime `r` lies above the sifting range, then

\[
\boxed{w(r)=1.}
\tag{3}
\]

For the ordinary one-dimensional sieve, the standard fundamental-lemma estimate gives, for fixed admissible sieve parameter `s=log D/log z`,

\[
\boxed{
\sum_{n\le N}w(n)\ll_s \frac{N}{\log z}+D.
}
\tag{4}
\]

Thus `w` supplies exactly the two structural properties for which Schlage-Puchta introduced the square `f=(1*g)^2`: nonnegativity for the weighted inner product and unit weight on the target shell primes, while retaining the expected `N/log z` diagonal scale.

For every Dirichlet character `chi`, the off-diagonal weighted character sum has the exact linear-sieve expansion

\[
\boxed{
S_\chi(N):=\sum_{n\le N}w(n)\chi(n)
=
\sum_{d\le D}\lambda_d^+\chi(d)M_\chi(N/d),
}
\tag{5}
\]

where

\[
M_\chi(X):=\sum_{m\le X}\chi(m).
\tag{6}
\]

Iwaniec's factorable modification, in the modern form recalled by Maynard, writes the relevant upper-bound linear-sieve coefficient sequence as a bounded finite linear combination of well-factorable sequences. For every factorization `D=UV`, each component can therefore be written

\[
\lambda^{(j)}=\alpha^{(j)}*\beta^{(j)},
\qquad
\operatorname{supp}\alpha^{(j)}\subseteq[1,U],
\quad
\operatorname{supp}\beta^{(j)}\subseteq[1,V],
\tag{7}
\]

with bounded factors. Substitution into `(5)` yields the exact pre-triangle bilinear form

\[
\boxed{
S_\chi(N)
=
\sum_j\sum_{uv\le D}
\alpha_u^{(j)}\beta_v^{(j)}
\chi(uv)M_\chi(N/(uv)).
}
\tag{8}
\]

This is a genuine new surviving representation for the current Mathia frontier. It does **not** resurrect the fake divisor-pair multiplicity ruled out by `MC-398` and `MC-404`: the variables `(u,v)` are a factorization of the **coefficient sequence**, not extra independent divisor-incidence data. Nor does it automatically reproduce Stadlmann's retained-phase mechanism, because complete multiplicativity still separates `chi(uvm)` and ordinary differencing in `m` removes the scalar `chi(uv)`. What changes is narrower and concrete: the prime-frame proof no longer has to pass through the lcm coefficients `C_g(ell)` of a quadratic Selberg square, and the off-diagonal is presented in a classical convolutional form on which dispersion, bilinear character-sum, or well-factorable technology can in principle act before an `ell^1` triangle inequality.

Therefore the accepted retained-variable clue has a specific live branch that was missing from `MC-397`--`MC-408`:

> replace the positive Selberg square by a positive well-factorable upper linear-sieve weight, preserve the same shell-prime frame, and test whether the convolution structure in `(8)` yields a source-character estimate stronger than the existing modewise/source-depth bound.

No such improved estimate is proved here. No estimate for `M(x)` follows.

## 1. Positivity does not require a square

The reason `f=(1*g)^2` is useful in Schlage-Puchta's argument is structural. It gives a nonnegative weight with `f(p)=1` on primes beyond the sieve cutoff, so one may define a weighted Hilbert-space product while leaving the prime-supported target vector unchanged.

An upper-bound sieve already has the first property by definition. For every integer `n`,

\[
\mathbf 1_{(n,P(z))=1}
\le
\sum_{\substack{d\mid n\\d\mid P(z)}}\lambda_d^+.
\tag{9}
\]

The right-hand side is `w(n)`. If `(n,P(z))>1`, the left side is zero, so `w(n)>=0`; if `(n,P(z))=1`, only `d=1` contributes and `w(n)=lambda_1^+=1`. This proves `(2)`.

In particular, every shell prime `r` larger than all sifting primes is coprime to `P(z)`, so `(3)` follows. Consequently the same prime-supported vector used in the Bombieri frame argument can be embedded in the weighted space with inner product

\[
\langle a,b\rangle_w
:=\sum_{n\le N}w(n)a_n\overline{b_n}.
\tag{10}
\]

The square was one convenient way to obtain positivity; it is not the only one.

For `A={1,...,N}`, the one-dimensional upper linear sieve gives

\[
\sum_{n\le N}w(n)
\ll_s N V(z)+D,
\qquad
V(z)=\prod_{p<z}\left(1-\frac1p\right),
\tag{11}
\]

and Mertens' product theorem gives `V(z) asymp 1/log z`, yielding `(4)`. The exact sieve constant is irrelevant to the representation question: the diagonal remains on the same `N/log` scale needed by the frame method.

## 2. The off-diagonal becomes a linear divisor hyperbola

For a Dirichlet character `chi`, insert `(1)` and exchange finite sums:

\[
\begin{aligned}
S_\chi(N)
&=\sum_{n\le N}\chi(n)\sum_{d\mid n}\lambda_d^+\\
&=\sum_{d\le D}\lambda_d^+
  \sum_{m\le N/d}\chi(dm)\\
&=\sum_{d\le D}\lambda_d^+\chi(d)M_\chi(N/d),
\end{aligned}
\tag{12}
\]

which is `(5)`. If `(d,q)>1`, both `chi(d)` and the corresponding terms vanish automatically under the standard Dirichlet-character convention, so no extra coprimality patch is needed.

Compare this with the squared Selberg expansion

\[
\sum_{\ell\le B^2}C_g(\ell)\chi(\ell)M_\chi(N/\ell)
\]

from `MC-399`. The analytic kernel is similar, but the coefficient family is not: the new `lambda_d^+` can be chosen from the classical well-factorable linear-sieve package rather than being the lcm-fiber closure of an arbitrary Selberg square.

This distinction survives the representation audit. `MC-404` proves that pointwise divisor incidence always admits a one-lcm normal form; `(5)` is already such a one-divisor normal form. The new information is not a second incidence label. It is the **external convolution law satisfied by the coefficients themselves**.

## 3. Well-factorability gives an exact pre-triangle bilinear form

Maynard recalls the classical Iwaniec construction as follows: standard sieve weights are not in general well-factorable, but a slight variant of the upper-bound beta-sieve weights is a finite linear combination of well-factorable sequences; in the linear-sieve case this is precisely the coefficient family used for well-factorable mean-value theorems.

For a well-factorable component and any chosen `D=UV`, write

\[
\lambda_d^{(j)}
=
\sum_{uv=d}\alpha_u^{(j)}\beta_v^{(j)}.
\tag{13}
\]

Substituting `(13)` into `(5)` gives `(8)` exactly. In particular, no bound such as

\[
\sum_d |\lambda_d^+|\,|M_\chi(N/d)|
\]

has yet been taken. The coefficient factorization is available **before** triangle inequality, Cauchy, dispersion, or any q-vdC step.

This is precisely the kind of structure that modern distribution theorems exploit in other sieve problems. Bombieri--Friedlander--Iwaniec used well-factorable weights to pass the square-root distribution barrier; Maynard extended the range and made the factorization structure explicit; Pascadi's 2025 work pushed related triply-well-factorable prime-distribution estimates to `5/8-o(1)`. Those theorems do not directly estimate `(8)`, because here the oscillatory object is a source Dirichlet character and `d` is a sieve-divisor variable rather than the modulus of a prime progression. They are prior-art evidence that the factorization is analytically meaningful, not a theorem transplant.

## 4. What remains separable and what genuinely changed

The source character remains completely multiplicative:

\[
\chi(uvm)=\chi(u)\chi(v)\chi(m).
\tag{14}
\]

Therefore an argument that merely writes three variables and then applies additive van der Corput only to `m` gains nothing from `(u,v)` in the source phase. The exact obstruction of `MC-399` still applies at that level.

The surviving coupling is instead in the coefficient convolution and moving hyperbola `uvm<=N`. Any real gain must exploit at least one of:

- bilinear cancellation across the factorable coefficient variables before absolute values are taken;
- a dispersion or large-sieve estimate whose diagonal/off-diagonal geometry depends on the factorization `D=UV`;
- a source-family estimate that averages the bilinear forms `(8)` collectively rather than paying the current modewise conductor-depth tariff;
- an additional congruence or translation generated after a Cauchy/Poisson/q-vdC transformation in which one factor remains arithmetic rather than a removable scalar.

If every proposed proof first replaces `(8)` by an `ell^1` sum of individual `M_chi(N/d)` bounds, then well-factorability has been discarded and the route reduces to the already-classified source-character problem.

## 5. Prior art and novelty boundary

The sieve ingredients are classical and no novelty is claimed for them.

- Henryk Iwaniec, *A new form of the error term in the linear sieve*, Acta Arithmetica **37** (1980), 307--320, DOI `10.4064/aa-37-1-307-320`, is the original factorable-linear-sieve source used by the later literature.
- James Maynard, *Primes in arithmetic progressions to large moduli II: Well-factorable estimates*, Memoirs of the AMS **306** (2025), no. 1543; arXiv:`2006.07088`. The introduction states explicitly that standard sieve weights are not generally well-factorable, recalls Iwaniec's well-factorable variant of the upper-bound beta-sieve, and identifies the linear-sieve upper weights as the important beta=1 case. Section 9 records their factorization structure.
- Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers*, arXiv:`2505.00653` (2025), proves `5/8-o(1)` distribution results using triply-well-factorable weights and improvements for well-factorable linear-sieve weights. It is cited only as modern evidence for the analytic power of the coefficient structure, not as an estimate for the present character sum.
- Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143--149, supplies the prime-frame/Selberg-square architecture used in `MC-377`.

The Mathia-specific contribution is the representation transplant: the exact prime-frame requirements are checked against the upper linear sieve and shown to survive, so the quadratic Selberg/lcm coefficient `C_g` is not a mandatory bottleneck of this branch. No claim is made that the resulting bilinear form `(8)` is new in analytic number theory, or that existing well-factorable distribution theorems already control it.

## Boundaries and falsification tests

- **Upper-bound property is load-bearing.** An arbitrary well-factorable sequence does not define a nonnegative Hilbert-space weight. The total coefficient sequence must remain an upper-bound sieve; factorable components may be signed individually.
- **Prime normalization requires the shell above the sifting primes.** Equation `(3)` uses that no nontrivial supported sieve divisor divides a target shell prime.
- **The diagonal estimate is a one-dimensional sieve statement.** It depends on choosing a standard admissible relation between `D` and `z`; no uniform claim over arbitrary `D,z` is made.
- **Well-factorability is coefficient structure, not sample multiplicity.** Treating `(u,v)` as independent arithmetic observations would repeat the error ruled out by `MC-404`.
- **Complete multiplicativity still kills a naive retained-phase argument.** Equation `(14)` means the first `m`-correlation does not retain `u` or `v` merely as source phases.
- **Existing BFI/Maynard/Pascadi theorems do not directly apply.** Their modulus/progression geometry differs from `(8)`. A valid transfer must verify the exact hypotheses of a bilinear/dispersion theorem for the source-character form.
- **No source-depth gain has yet been proved.** The decisive next test is analytic: derive a bound for `(8)`, preferably collectively over the source family, that is strictly stronger than applying current individual character bounds after triangle inequality.
- **No RH input or conclusion.** The construction is finite sieve/frame algebra and does not use analytic continuation of `1/zeta`, a zero-free region, or an estimate for the Mertens function.

## Consequence for the research line

`MC-397`--`MC-404` correctly show that the standard positive Selberg square collapses to a one-lcm coefficient and that incidence-only attempts cannot recover an extra arithmetic dimension. The present result identifies a different route that passes those exact representation checks: **change the positive sieve majorant itself**.

The next useful calculation should not further manipulate `C_g(ell)`. It should take a concrete Iwaniec/linear-sieve factorable upper weight, insert its factorization into the source-character off-diagonal `(8)`, and determine whether any available bilinear character-sum, dispersion, or family large-sieve estimate preserves the factorization long enough to beat the existing source-depth cost. A negative theorem showing that every such factorable form collapses back to the same modewise barrier would also be a substantive closure result.