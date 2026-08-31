# WP-075 — Positive shifted-resolvent cover defects mix log degree with digamma, but exact finite weights force zero shift

## Claim

Continue the pointed-cover Hardy-coordinate geometry of `WP-073` and `WP-074`. Let

\[
\widetilde W_n e_k
=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
L=N+\frac12I,
\qquad n\ge2,
\]

so that `\widetilde W_n` is an isometry and

\[
\widetilde W_n^*L\widetilde W_n=nL.
\]

For every real shift `c>-1/2`, define the normalized shifted-resolvent Jensen defect

\[
\boxed{
R_{n,c}
:=
n\widetilde W_n^*(L+cI)^{-1}\widetilde W_n
-
\left(L+\frac cn I\right)^{-1}.
}
\tag{1}
\]

Then:

1. `R_{n,c}` is a strictly positive trace-class diagonal operator;
2. its trace is exactly
   \[
   \boxed{
   \tau_n(c):=\operatorname{Tr}R_{n,c}
   =\log n
   +\psi\!\left(\frac12+\frac cn\right)
   -\psi\!\left(\frac12+c\right);
   }
   \tag{2}
   \]
3. `\tau_n(0)=\log n`, recovering the positive log-degree defect of `WP-074`;
4. for every `n>1`,
   \[
   \boxed{
   \tau_n(c)=\log n
   \quad\Longleftrightarrow\quad
   c=0;
   }
   \tag{3}
   \]
5. if one inserts the archimedean spectral shift `c=(s-1)/2`, then for real `s>0`
   \[
   \tau_n\!\left(\frac{s-1}{2}\right)
   =
   \log n
   +\psi\!\left(\frac{n+s-1}{2n}\right)
   -\psi(s/2),
   \tag{4}
   \]
   so the same positive defect contains the nonconstant digamma profile, but it also changes the finite coefficient away from `\log n` by an unavoidable degree-dependent term.

Consequently the most direct positive attempt to merge the two strongest structures of `WP-074` fails an exact compatibility test. On a primitive prime ray, replacing `Q_p` by `R_{p,c}` produces the positive kernel

\[
\tau_p(c)\,p^{-|k-\ell|/2},
\]

whose first row equals the required finite Weil weight `(\log p)p^{-k/2}` for every `k` **if and only if `c=0`**. But at `c=0` the digamma correction in (2) vanishes identically. Turning on the shift needed to expose `\psi` necessarily contaminates every finite prime coefficient before any global assembly is formed.

There is a second exact boundary. For `0<\alpha<1`, the canonical inverse-power defects

\[
Q_{n,\alpha}
:=
n^\alpha\widetilde W_n^*L^{-\alpha}\widetilde W_n-L^{-\alpha}
\succeq0
\tag{5}
\]

are positive Mellin mixtures of the same shifted-resolvent defects and satisfy

\[
\boxed{
\operatorname{Tr}Q_{n,\alpha}
=
\bigl(n^{\alpha-1}-1\bigr)\zeta(\alpha,1/2).
}
\tag{6}
\]

The endpoint `\alpha\uparrow1` is exactly `\log n`; every fixed interior `0<\alpha<1` instead has a bounded large-degree trace. Thus the log-degree term of `WP-074` is a genuine positive trace, but inside this canonical Stieltjes/Mellin family it is an endpoint phenomenon rather than a robust positive finite--archimedean coupling.

**Evidence status:** `EXACT-DERIVED + POSITIVE-FAMILY + DECISIVE-COMPATIBILITY-OBSTRUCTION + CLASSICAL-FUNCTIONAL-CALCULUS`.

## 1. The shifted defect is positive without analytic continuation

Put

\[
A_c=L+cI>0.
\]

Since

\[
\widetilde W_n^*A_c\widetilde W_n=nL+cI
=n\left(L+\frac cn I\right),
\]

the operator-convexity of `x\mapsto x^{-1}` gives

\[
\widetilde W_n^*A_c^{-1}\widetilde W_n
\succeq
(\widetilde W_n^*A_c\widetilde W_n)^{-1}
=
\frac1n\left(L+\frac cn I\right)^{-1}.
\]

Multiplication by `n` proves (1) is positive.

Here no abstract operator theorem is needed. In the Hardy basis, `R_{n,c}` is diagonal. Writing

\[
a_{r,c}:=\frac{r+1/2+c}{n},
\]

one obtains

\[
R_{n,c}e_k=r_{n,c}(k)e_k,
\]

with

\[
\boxed{
r_{n,c}(k)
=
\frac1n\sum_{r=0}^{n-1}
\frac1{k+a_{r,c}}
-
\frac1{k+1/2+c/n}.
}
\tag{7}
\]

The arithmetic mean of the `n` positive numbers `k+a_{r,c}` is exactly

\[
k+\frac12+\frac cn.
\]

Since `x\mapsto1/x` is strictly convex, (7) is strictly positive for every `k` when `n>1`. The centered first moment vanishes, so Taylor expansion about the block mean gives

\[
r_{n,c}(k)=O_{n,c}(k^{-3}).
\]

Hence `R_{n,c}` is positive trace class. Positivity is therefore a literal block-Jensen theorem inside the pointed-cover geometry, not a property obtained by zeta regularization or continuation.

## 2. The trace is an exact log-degree plus digamma difference

For a cutoff `M`, reindexing the first term of (1) block by block gives

\[
\begin{aligned}
\sum_{k=0}^{M-1}r_{n,c}(k)
&=
\sum_{j=0}^{nM-1}\frac1{j+1/2+c}
-
\sum_{k=0}^{M-1}\frac1{k+1/2+c/n}\\
&=
\psi(nM+1/2+c)-\psi(1/2+c)\\
&\qquad
-\psi(M+1/2+c/n)+\psi(1/2+c/n).
\end{aligned}
\tag{8}
\]

Using `\psi(x)=\log x+O(x^{-1})`, the two large-cutoff terms differ by `\log n+o(1)`. Letting `M\to\infty` proves (2):

\[
\operatorname{Tr}R_{n,c}
=
\log n
+\psi(1/2+c/n)-\psi(1/2+c).
\]

At `c=0`, the two digamma values coincide, so

\[
R_{n,0}
=
n\widetilde W_n^*L^{-1}\widetilde W_n-L^{-1}
=Q_n
\]

and `\operatorname{Tr}R_{n,0}=\log n`, exactly `WP-074`.

The formula is also a useful adversarial check on the interpretation of that logarithm. The same block-refinement geometry does not merely happen to have a resolvent whose trace is logarithmic: once the spectral origin is moved while preserving positivity, the logarithm is inseparably accompanied by a digamma correction.

## 3. Exact finite Weil weights uniquely force the zero shift

The digamma function is strictly increasing on `(0,\infty)`. Therefore for `n>1`,

\[
\psi(1/2+c/n)=\psi(1/2+c)
\]

holds if and only if

\[
\frac cn=c,
\]

which is equivalent to `c=0`. This proves (3).

Now specialize to a primitive prime generator `p`. The positive orbit vectors from `WP-074` obey

\[
\langle u_{p,k},u_{p,\ell}\rangle
=p^{-|k-\ell|/2}.
\]

Multiplying this Gram matrix by the positive scalar `\tau_p(c)` gives another positive Gram kernel,

\[
G_{p,c}(k,\ell)
=
\tau_p(c)p^{-|k-\ell|/2}.
\tag{9}
\]

Its first row is

\[
G_{p,c}(0,k)=\tau_p(c)p^{-k/2}.
\]

The finite explicit-formula coefficient requires

\[
G_{p,c}(0,k)
=(\log p)p^{-k/2}
\]

for every `k`. By (3), this forces `c=0` for every prime independently. Even allowing a prime-dependent shift `c_p` does not evade the conclusion: exact coefficient matching gives `c_p=0` one prime at a time.

Thus there is no nonzero shifted member of this positive family that simultaneously preserves the exact local finite weight and contributes a digamma correction. A subsequent scalar rescaling or subtraction could of course restore `\log p`, but that would insert a degree-dependent correction after seeing the target coefficient and would no longer inherit the sign theorem from (1).

## 4. The archimedean shift appears, but only after finite-place contamination

The Riemann archimedean logarithmic derivative contains

\[
\frac{d}{ds}\log\!\left(\pi^{-s/2}\Gamma(s/2)\right)
=
\frac12\psi(s/2)-\frac12\log\pi.
\tag{10}
\]

The shift

\[
c=\frac{s-1}{2}
\]

is therefore the canonical test of whether the positive resolvent defect can produce the Gamma profile without leaving the same geometry. Substitution in (2) gives (4):

\[
\tau_n((s-1)/2)
=
\log n
+
\psi\!\left(\frac{n+s-1}{2n}\right)
-
\psi(s/2).
\]

For fixed real `s>0`, this is the trace of a genuinely positive operator. Moreover,

\[
\tau_n((s-1)/2)-\log n
\longrightarrow
\psi(1/2)-\psi(s/2)
\qquad(n\to\infty).
\tag{11}
\]

So the nonconstant Gamma/digamma shape does emerge from **the same positive cover-resolvent construction**. This is stronger than merely observing the half-integer spectrum of `L`.

But the exact local-to-global audit fails in two independent ways.

First, at finite `n=p` the correction

\[
\psi\!\left(\frac{p+s-1}{2p}\right)-\psi(s/2)
\]

is mixed with the prime coefficient itself. It is neither a universal archimedean term nor zero. Extracting the asymptotic residual (11) requires subtracting `\log n` from a positive trace; the residual is not the trace of the positive defect and does not inherit its sign.

Second, on the critical line `s=1/2+it` the shift `c=(s-1)/2` is complex. Then `L+cI` is not self-adjoint and (1) is no longer a positive self-adjoint operator. The real-axis Jensen theorem therefore cannot be analytically continued into a Weil sign theorem. This is the same categorical boundary already visible in `WP-015` and in the relative-resolvent discussion of `WP-074`: analytic continuation of a response can preserve an exact formula while losing the independent real positivity that the research mandate requires.

Equation (10) also contains the normalization `-\tfrac12\log\pi`, while the polar `s=0,1` terms remain absent. Neither is forced by `R_{n,c}`.

## 5. The whole inverse-power/Stieltjes closure remains degree-only

The shifted resolvent is not an isolated choice. For `0<\alpha<1`, use the classical Stieltjes representation

\[
x^{-\alpha}
=
\frac{\sin(\pi\alpha)}\pi
\int_0^\infty
\frac{c^{-\alpha}}{x+c}\,dc.
\tag{12}
\]

Combining (12) with (1) gives the exact positive mixture

\[
\boxed{
Q_{n,\alpha}
=
\frac{\sin(\pi\alpha)}\pi
n^{\alpha-1}
\int_0^\infty c^{-\alpha}R_{n,c}\,dc
\succeq0.
}
\tag{13}
\]

Directly in the Hardy basis,

\[
Q_{n,\alpha}e_k
=
\left[
\frac1n\sum_{r=0}^{n-1}
\left(k+\frac{r+1/2}{n}\right)^{-\alpha}
-
(k+1/2)^{-\alpha}
\right]e_k.
\tag{14}
\]

Again positivity is simply strict convexity of `x^{-\alpha}` on each block, and the centered first moment makes the diagonal `O(k^{-\alpha-2})`, hence trace class.

For `\Re\alpha>1`, residue-class reindexing gives the trace immediately in terms of the half-shift Hurwitz zeta function. The trace series in (14) is already convergent for `\Re\alpha>-1`, so the same identity extends across the removable region and for `0<\alpha<1` gives

\[
\operatorname{Tr}Q_{n,\alpha}
=
(n^{\alpha-1}-1)\zeta(\alpha,1/2).
\tag{15}
\]

Equivalently, finite partial sums plus Euler--Maclaurin give (15) without assigning values to any divergent positive series separately. The endpoint is

\[
\lim_{\alpha\uparrow1}
(n^{\alpha-1}-1)\zeta(\alpha,1/2)
=
\log n,
\tag{16}
\]

because the Hurwitz zeta function has residue `1` at `\alpha=1`. Thus `WP-074` is the endpoint of this positive family.

For every fixed `0<\alpha<1`, however,

\[
\operatorname{Tr}Q_{n,\alpha}
\longrightarrow
-\zeta(\alpha,1/2)
<\infty
\qquad(n\to\infty).
\tag{17}
\]

The logarithmic tangent at the opposite endpoint is also universal. Since `Q_{n,0}=0`, differentiating (15) at `\alpha=0` and using

\[
\zeta(0,1/2)=0,
\qquad
\zeta'(0,1/2)=-\frac12\log2,
\]

gives

\[
\boxed{
\operatorname{Tr}\left.
\frac{d}{d\alpha}Q_{n,\alpha}
\right|_{\alpha=0}
=
\frac12\left(1-\frac1n\right)\log2.
}
\tag{18}
\]

So the most natural logarithmic/Jensen tangent actually forgets the logarithmic degree and collapses to a bounded dyadic constant. This strengthens the interpretation of (16): within the canonical positive Stieltjes closure of the forced scale operator, `\log n` is special to the inverse-scale endpoint, not a generic entropy or Mellin response that might independently supply the missing global counterterms.

## 6. Matched controls and prior-art audit

Every calculation above depends only on the degree-`n` block replication `\widetilde W_n` and the forced half-integer scale operator `L`. It does not use primality, cyclotomic coefficients, rational-prime incidence, zeta zeros, or a functional equation. Any non-arithmetic degree-`n` cyclic-cover model with the same pointed Hardy replication has the same operators, traces, and digamma formulas.

This matters in three ways.

- **Prime-power support remains external.** `R_{n,c}` exists for every integer degree and its trace is nonzero for generic composites. As in `WP-074`, the primitive-prime-ray decomposition is needed before the finite explicit-formula support appears.
- **The Weil autocorrelation obstruction remains.** At `c=0`, exact finite weights return, but the prime-ray Gram is exactly the positive Poisson kernel of `WP-074`; converting it to the finite Weil summand still requires the indefinite `I-P_r` subtraction identified in `WP-005` and `WP-022`. At `c\ne0`, only the positive scalar prefactor changes, and it changes to the wrong finite coefficient.
- **The archimedean shape is universal cover spectroscopy.** The digamma in (2) comes from the half-integer spectrum of `L` and elementary block refinement. It is therefore structural, but not arithmetic evidence by itself.

The functional-analytic ingredients are classical. The positivity of (1) is a special diagonal case of Jensen's operator inequality for the convex inverse, and the formulas involving `\psi`, `\zeta(\alpha,1/2)`, and `\zeta'(0,1/2)` are standard Hurwitz-zeta/digamma identities (the line already retains NIST DLMF §25.11 as a literature anchor). The directed novelty search around operator-Jensen defects, Hurwitz-zeta traces, block-replication isometries, and local-Dirichlet composition operators did not identify a source claiming this Mathia-specific finite-versus-archimedean compatibility test. That absence is not used as evidence of novelty.

Accordingly no novelty is claimed for Jensen convexity, Stieltjes functional calculus, the digamma function, Hurwitz-zeta multiplication, or the half-integer spectral zeta. The durable content here is the exact **restriction** inside the already-forced `WP-073`/`WP-074` geometry: the single positive deformation that exposes the Gamma profile cannot retain the exact finite coefficient except at the unique point where that profile disappears.

## 7. Exact falsification surface

The claim can be refuted by any of the following exact failures:

1. failure of the diagonal formula (7) for the `WP-074` block isometry;
2. a real `c>-1/2` and `n>1` for which some diagonal entry of `R_{n,c}` is negative;
3. failure of the cutoff identity (8) or of the trace formula (2);
4. a nonzero real `c` satisfying `\tau_n(c)=\log n` for some `n>1`;
5. failure of the prime-ray first-row calculation (9);
6. failure of the positive Stieltjes mixture (13) or trace formula (15);
7. a canonical, positivity-preserving extraction from the same `R_{n,c}` family that separates the degree-dependent correction into an exact prime-independent archimedean term while leaving every finite coefficient `(\log p)p^{-k/2}` unchanged.

Item 7 is the genuine escape hatch. Merely subtracting `\log n`, fitting a prime-dependent scalar, analytically continuing `c` to a complex value, or importing the desired Gamma/polar term does not satisfy it.

## Research consequence

`WP-074` left a particularly tempting possibility: the same forced half-integer scale operator already gave both a positive trace `\log p` and an exact digamma relative trace, so perhaps shifting its positive inverse-scale defect would merge the finite and archimedean sectors before the sign theorem.

`WP-075` closes that direct route. The merger exists algebraically and remains positive on the real resolvent axis,

\[
\boxed{
R_{n,c}\succeq0
\quad\Longrightarrow\quad
\operatorname{Tr}R_{n,c}
=
\log n+\text{digamma correction},
}
\]

but **exact finite-place matching forces `c=0`**, where the correction vanishes. Isolating the Gamma-shaped residual requires a subtraction that is not inherited from the positive operator, while continuation to the critical line destroys self-adjoint positivity. The larger inverse-power family confirms that this is not an accident of one resolvent shift: it remains universal degree geometry, and only its inverse-scale endpoint carries unbounded `\log n`.

A viable continuation must therefore leave this scalar functional-calculus deformation class. It needs a genuinely coupled finite--archimedean construction — for example a nonseparable boundary quotient, compression, cohomological/intersection pairing, or cross-prime operator sector — in which the exact finite weights and Gamma/polar terms are components of one object **before** positivity is invoked, rather than different scalar traces of the same half-integer scale operator.