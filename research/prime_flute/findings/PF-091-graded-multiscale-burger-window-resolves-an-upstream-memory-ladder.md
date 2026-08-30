# PF-091 — a graded Burger window resolves an arbitrarily long upstream-memory ladder

**Status:** `POSITIVE / RIGOROUS FINITE-TANGENT THEOREM + CONDITIONAL PRIME-REALIZATION GATE`.

PF-090 promoted the first two-scale Feshbach correction

\[
-\frac{3}{16\pi^2}\frac{b^2}{a}
\]

from the weighted path to the true hyperbolic Laplacian, provided the two necks obey the moderate hierarchy

\[
a^{3/2}\ll b\ll a.
\]

The same idea extends to an arbitrary fixed chain of pairs of pants.  There is a nonempty **graded multiscale window** in which Burger's single quantitative surface-to-graph estimate is simultaneously fine enough to resolve, at every weak scale, the first correction caused by the immediately stronger upstream neck.  Thus the true Laplace spectrum can carry an arbitrarily long finite ladder of second-order interscale memories.

The result is intrinsic to the exact hyperbolic tangent.  The prime-flute consequence is conditional only at the last arithmetic step: the current Pintz/Maynard extraction proves arbitrarily strong hierarchical tangents, but it does not yet force this moderate graded upper control for the unknown selected prime subset.

## 1. Hyperbolic chain and exact graph reduction

Fix `N>=3`.  Let `Y(w)` be a finite-area genus-zero hyperbolic surface of type

\[
S_{0,N+2}
\]

obtained from `N` pairs of pants in a path.  Let the `N-1` internal separating geodesics have lengths

\[
w_1>w_2>\cdots>w_{N-1}>0,
\]

all tending to zero.  The zero-twist prime tangent is a special case; the statement below only needs the lengths.

Burger's dual weighted graph is the ordinary weighted path Laplacian

\[
G(w)=\sum_{j=1}^{N-1}w_j(e_j-e_{j+1})(e_j-e_{j+1})^T.
\]

Write the positive graph eigenvalue associated asymptotically with the edge `w_j` as `mu^(j)`; in increasing spectral order this is `mu_{N-j}`.  PF-054 gives the first-order law

\[
\mu^{(j)}\sim \frac{j+1}{j}w_j.
\]

PF-080's Feshbach/effective-resistance expansion refines this to

\[
\mu^{(j)}=
\frac{j+1}{j}w_j
+\frac{j}{j+1}w_{j+1}
-\frac{j+1}{j^3}w_j^2
\sum_{m<j}\frac{m^2}{w_m}
+\text{higher-order terms},
\]

where the downstream term is absent for `j=N-1`.

The zero mode in the resistance identity must be fixed explicitly. Let `L_{\{1,\ldots,j\}}` be the connected weighted path Laplacian on vertices `1,...,j`, define the centered source

\[
q_j:=e_j-\frac1j\mathbf 1\in\mathbf 1^\perp,
\]

and let `L_{\{1,\ldots,j\}}^+` denote its Moore--Penrose inverse, so

\[
L_{\{1,\ldots,j\}}^+\mathbf 1=0.
\]

Since `e_j=q_j+\mathbf 1/j`, the usual shorthand is exactly the gauge-invariant centered quadratic form:

\[
e_j^TL_{\{1,\ldots,j\}}^+e_j
=q_j^TL_{\{1,\ldots,j\}}^+q_j.
\]

The centered equation `L_{\{1,\ldots,j\}}u=q_j` is solvable modulo constants. Across the edge `m\leftrightarrow m+1`, conservation gives current magnitude `m/j`; hence the Dirichlet energy is

\[
R_j:=q_j^TL_{\{1,\ldots,j\}}^+q_j
=e_j^TL_{\{1,\ldots,j\}}^+e_j
=\sum_{m=1}^{j-1}\frac{(m/j)^2}{w_m}
=\frac1{j^2}\sum_{m=1}^{j-1}\frac{m^2}{w_m}.
\]

Thus every later use of `e_j^TL^+e_j` in this finding is shorthand under this Moore--Penrose zero-mode convention.

For `j=2` this reduces to the PF-081/PF-090 coefficient `-3w_2^2/(8w_1)`.

## 2. A graded moderate hierarchy

Put

\[
\varepsilon:=w_1\to0,
\qquad
r_j:=\frac{w_j}{w_{j-1}},\quad j\ge2.
\]

Assume, for every fixed `j=2,...,N-1`,

\[
r_j\to0,
\]

and impose the two additional scale conditions

\[
\boxed{\sqrt{w_1}=o(r_j)}
\]

and, whenever `j<N-1`,

\[
\boxed{r_{j+1}=o(r_j)}.
\]

These conditions are compatible for any fixed `N`.  A particularly transparent family is

\[
\boxed{
r_j=\varepsilon^{\alpha_j},
\qquad
0<\alpha_2<\alpha_3<\cdots<\alpha_{N-1}<\frac12.
}
\]

Thus the necks are genuinely hierarchical, and the hierarchy itself becomes successively stronger, but every adjacent ratio remains larger than Burger's relative error scale `sqrt(w_1)`.

## 3. The graph correction reduces to the immediately previous neck

Because

\[
\frac{w_{j-1}}{w_{j-2}}=r_{j-1}\to0,
\]

the effective-resistance sum is dominated by its last term:

\[
\sum_{m<j}\frac{m^2}{w_m}
=\frac{(j-1)^2}{w_{j-1}}(1+o(1)).
\]

The downstream term obeys

\[
\frac{w_{j+1}}{w_j^2/w_{j-1}}
=\frac{r_{j+1}}{r_j}\to0.
\]

The next Feshbach terms are smaller by an additional factor `r_j`, while the ordinary local collar corrections of size `w_j^2 |log w_j|` satisfy

\[
\frac{w_j^2|\log w_j|}{w_j^2/w_{j-1}}
=w_{j-1}|\log w_j|\to0
\]

for the displayed power-type window (and more generally under the evident mild logarithmic condition).

Consequently the weighted path has, simultaneously for every `j=2,...,N-1`,

\[
\boxed{
\mu^{(j)}
=
\frac{j+1}{j}w_j
-
\frac{(j+1)(j-1)^2}{j^3}
\frac{w_j^2}{w_{j-1}}
+o\!\left(\frac{w_j^2}{w_{j-1}}\right).
}
\]

The correction at the `j`-th weak scale therefore remembers the preceding neck, not only the current one.

## 4. Burger resolves every memory term on the true surface

Burger's quantitative theorem applies uniformly for fixed topology.  For the maximal pants decomposition above,

\[
l(A)=w_1,
\qquad
L(A)=2\operatorname{arsinh}(1),
\]

exactly as in PF-090, hence the cusp-neighborhood parameter satisfies

\[
\epsilon_B\asymp w_1.
\]

For each small eigenvalue,

\[
\lambda^{(j)}(Y(w))
=
\frac{\mu^{(j)}}{2\pi^2}
+O\!\left(\mu^{(j)}\sqrt{w_1}\right).
\]

Since `mu^(j)~((j+1)/j)w_j`, the Burger error compared with the upstream term is

\[
\frac{w_j\sqrt{w_1}}{w_j^2/w_{j-1}}
=
\frac{\sqrt{w_1}}{r_j}
\longrightarrow0.
\]

Therefore the actual hyperbolic Laplacian satisfies

\[
\boxed{
\lambda^{(j)}(Y(w))
=
\frac{j+1}{2\pi^2j}w_j
-
\frac{(j+1)(j-1)^2}{2\pi^2j^3}
\frac{w_j^2}{w_{j-1}}
+o\!\left(\frac{w_j^2}{w_{j-1}}\right),
}
\]

simultaneously for `j=2,...,N-1`.

Equivalently,

\[
\boxed{
\frac{
\frac{j+1}{2\pi^2j}w_j-\lambda^{(j)}
}{w_j^2/w_{j-1}}
\longrightarrow
\frac{(j+1)(j-1)^2}{2\pi^2j^3}.
}
\]

This is a genuine surface theorem, not a Ritz or graph-only statement.

For every sufficiently small eigenvalue put

\[
\lambda^{(j)}=s_j(1-s_j),\qquad s_j\to1.
\]

Since `(lambda^(j))^2=o(w_j^2/w_{j-1})` in the hierarchy, the same correction appears with opposite sign in the associated real resolvent-pole parameter:

\[
\boxed{
s_j
=1-
\frac{j+1}{2\pi^2j}w_j
+
\frac{(j+1)(j-1)^2}{2\pi^2j^3}
\frac{w_j^2}{w_{j-1}}
+o\!\left(\frac{w_j^2}{w_{j-1}}\right).
}
\]

No assertion is made that every individual cusp-scattering entry must display every pole; the resolvent statement is intrinsic.

## 5. Exact prime-circle geometry and cuff law

For an isolated ordered prime tangent with consecutive internal gaps `d_1,d_2,...`, the separating necks are defined by the **exact orthogonal-circle cross-ratios**.  In the hierarchical regime PF-054 gives

\[
w_j
=4\sqrt{\frac{d_j}{d_{j+1}}}(1+o(1)).
\]

Thus

\[
\frac{w_j^2}{w_{j-1}}
=
4\,
\frac{d_j^{3/2}}{d_{j+1}\sqrt{d_{j-1}}}
(1+o(1)).
\]

The first correction is therefore a genuine three-gap quantity; it is not a restatement of the current adjacent ratio.

For occurrences near prime scale `P`, write the adjacent distinguished-cuff contrasts

\[
C_j:=\ell_j-\ell_{j+1}.
\]

Since

\[
w_j=4e^{-C_j/4}(1+o(1)),
\]

the true surface law becomes

\[
\boxed{
\lambda^{(j)}
=
\frac{2(j+1)}{\pi^2j}e^{-C_j/4}
-
\frac{2(j+1)(j-1)^2}{\pi^2j^3}
 e^{-(2C_j-C_{j-1})/4}
+o\!\left(e^{-(2C_j-C_{j-1})/4}\right).
}
\]

The leading term sees only the current cuff contrast `C_j`.  The first spectrally resolvable correction sees the ordered pair `(C_{j-1},C_j)`.  Repeating this at successive scales gives a finite **spectral memory ladder**.

For `j=2` the formula is exactly PF-090:

\[
\lambda_{\rm weak}
=
\frac3{\pi^2}e^{-C_2/4}
-
\frac3{4\pi^2}e^{-(2C_2-C_1)/4}
+o(\cdots).
\]

## 6. Interior/exterior duality

Nothing in the theorem chooses an ambient side.  The `w_j` are the exact separating lengths determined by ordered cross-ratios of the orthogonal-circle configuration.  Ambient inversion exchanges the interior and exterior drawings while preserving those cross-ratios and hence every `w_j` and every coefficient above.  As in PF-017, the duality is geometric representation data, not a second intrinsic spectrum.

## 7. Serious novelty check

Known ingredients, for which no novelty is claimed:

- Burger, *Small eigenvalues of Riemann surfaces and graphs*, Math. Z. 205 (1990), gives the quantitative weighted-graph approximation with a relative `O(sqrt(epsilon))` control for fixed topology.
- Feshbach/Schur complement and effective resistance on a weighted path are standard finite-dimensional perturbation theory.
- Große--Rupflin, *Sharp eigenvalue estimates on degenerating surfaces* (2019), resolve much finer information for a **single** disconnecting collar under a uniform lower injectivity bound away from that collar.
- Chaudhary's Oxford DPhil thesis (2021) treats **multiple** collapsing geodesics and proves first-order dependence of the small eigenvalues on the collapsing disconnecting lengths and topology.
- Erchenko--Jakobson--Tsypin, arXiv:2604.26308 (29 April 2026), studies flexibility/inverse constraints for weighted graph spectra arising from pants decompositions; its surface input is again the first-order graph approximation.

Targeted searches through August 2026 for combinations of

```text
multiple collapsing geodesics + second order small eigenvalues,
effective resistance + degenerating hyperbolic surface eigenvalues,
multiscale pinching + second-order weighted graph correction,
hierarchical collars + Laplace eigenvalue asymptotics
```

did not locate the displayed surface-level coefficient or an arbitrary-length nested memory ladder.

The candidate-new statement is deliberately narrow: **Burger's classical quantitative error is already strong enough, in the graded window `sqrt(w_1)<<r_j<<1`, to promote the effective-resistance correction at every weak graph scale to the corresponding second asymptotic term of the true hyperbolic Laplacian.**  PF-090 is the two-neck instance; PF-091 identifies a nonempty regime where this can be done simultaneously for arbitrarily many fixed necks.

This does not claim a new general multi-collar surgery calculus, nor does it identify Riemann zeros.

## 8. Remaining prime-realization gate

The exact prime-flute consequence is not yet unconditional at arbitrary ladder length.  PF-046/PF-054 can force recurrent isolated prime patterns with arbitrarily strong scale separation, but the Maynard/Pintz step leaves the selected candidate subset uncontrolled.  The present Burger-resolvable window requires an **upper** hierarchy condition as well:

\[
\sqrt{w_1}\ll \frac{w_j}{w_{j-1}}\ll1.
\]

The simple power model

\[
r_j=w_1^{\alpha_j},
\qquad
0<\alpha_2<\cdots<\alpha_{N-1}<1/2
\]

shows that the geometric/spectral window is nonempty.  What is not yet proved is that an isolated recurrent block of consecutive primes can be forced into this graded window after the sieve chooses its surviving subset.

There are therefore two clean ways to close the remaining gate:

1. an arithmetic theorem giving enough control of several consecutive selected prime gaps to realize the graded moderate hierarchy; or
2. a sharper multi-collar surface estimate that lowers Burger's `sqrt(w_1)` resolution floor and thereby reaches the super-hierarchical patterns already supplied by PF-054.

## References

- Marc Burger, *Small eigenvalues of Riemann surfaces and graphs*, Math. Z. 205 (1990), 395--420. DOI 10.1007/BF02571252. Primary copy: https://people.math.ethz.ch/~burger/pub/1990_Small_eigenvalues.pdf
- Nadine Große and Melanie Rupflin, *Sharp eigenvalue estimates on degenerating surfaces*, Comm. PDE 44 (2019), 573--612; arXiv:1701.08491.
- Asad Chaudhary, *Estimates for small eigenvalues of the Laplacian and conformal Laplacian on closed manifolds*, Oxford DPhil thesis (2021), DOI 10.5287/ora-6gq1r27gd.
- Alena Erchenko, Dmitry Jakobson, Allison Tsypin, *Flexibility of eigenvalues for graph Laplacians arising from genus 3 surfaces*, arXiv:2604.26308 (submitted 29 April 2026).
