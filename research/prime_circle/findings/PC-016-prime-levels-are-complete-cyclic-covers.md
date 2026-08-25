# PC-016 — prime levels are exactly the levels where the new-vertex sphere is the complete cyclic cover

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`.

This is an exact two-dimensional reformulation of the original "all non-common vertices are new" observation. The covering theory itself is classical; the candidate new structure is to organize the birth shells as hyperbolic punctured spheres and distinguish exponent growth from introduction of a new prime by whether the power map remains an honest cover.

## 1. Spherical birth surfaces

Let

\[
\mu_n^*=\{\zeta\in\mathbb C:\operatorname{ord}(\zeta)=n\}
\]

be the vertices born at level \(n\). On the stereographic sphere, keep the two poles \(0,\infty\) and the common polygon vertex \(1\) as distinguished points. Define

\[
B:=\widehat{\mathbb C}\setminus\{0,1,\infty\}
\]

and the anchored birth surface

\[
X_n^{\mathrm{birth}}
:=
\widehat{\mathbb C}\setminus
\bigl(\{0,1,\infty\}\cup\mu_n^*\bigr),
\qquad n>1.
\]

Since \(1\notin\mu_n^*\) for \(n>1\), this has exactly \(\varphi(n)+3\) punctures.

Let

\[
F_n(z)=z^n.
\]

The complete preimage of the thrice-punctured sphere is

\[
F_n^{-1}(B)
=
\widehat{\mathbb C}\setminus
\bigl(\{0,\infty\}\cup\mu_n\bigr),
\]

because \(F_n^{-1}(1)=\mu_n\).

Therefore

\[
X_n^{\mathrm{birth}}=F_n^{-1}(B)
\]

if and only if

\[
\mu_n=\{1\}\sqcup\mu_n^*.
\]

For \(n>1\), that is equivalent to primality. Hence

\[
\boxed{
n\text{ prime}
\iff
F_n:X_n^{\mathrm{birth}}\longrightarrow B
\text{ is an unbranched regular cyclic cover of degree }n.
}
\]

The forward implication is especially geometric: at a prime level every non-common polygon vertex is a puncture in the full fiber over the single base puncture \(1\), so nothing has to be filled or deleted to obtain the natural cover.

For composite \(n\), the imprimitive non-common roots remain ordinary points of \(X_n^{\mathrm{birth}}\) but map to the missing point \(1\in\widehat{\mathbb C}\setminus B\). Thus the same power map does not even define a map \(X_n^{\mathrm{birth}}\to B\).

## 2. Hyperbolic consequence at prime levels

The thrice-punctured sphere \(B\) has its unique complete finite-area hyperbolic metric. If \(p\) is prime, uniqueness of the complete Poincare metric gives

\[
\boxed{g_{X_p}=F_p^*g_B.}
\]

The deck group is

\[
\operatorname{Deck}(X_p/B)\cong C_p,
\qquad
z\mapsto\zeta_p z.
\]

Thus prime levels carry a canonical spectral package with no extra geometric choices:

- a degree-\(p\) regular hyperbolic cover of one fixed base surface;
- a \(C_p\)-decomposition of \(L^2(X_p)\) into character sectors;
- the corresponding decomposition of the Laplacian/scattering problem;
- Venkov–Zograf / Artin-type factorization of Selberg zeta and scattering determinants into twisted objects on the base.

These factorization theorems for finite-index Fuchsian covers are classical and are **not** claimed as new. The potentially useful point is that the original new-vertex rule selects exactly those levels at which the birth surface itself, rather than an artificially completed full-root surface, belongs to this regular-cover spectral family.

As a check, \(X_p\) is a sphere with \(p+2\) punctures, so

\[
\operatorname{Area}(X_p)=2\pi p,
\]

exactly \(p\) times the area \(2\pi\) of the thrice-punctured sphere.

## 3. A stronger multiplicative dichotomy: old prime versus new prime

For the unanchored primitive-shell surface

\[
S_n:=
\widehat{\mathbb C}\setminus
\bigl(\{0,\infty\}\cup\mu_n^*\bigr),
\]

consider multiplication of the level by a prime \(p\). The exact order formula for a power gives

\[
F_p^{-1}(\mu_n^*)
=
\begin{cases}
\mu_{np}^*,&p\mid n,\\[1mm]
\mu_n^*\sqcup\mu_{np}^*,&p\nmid n.
\end{cases}
\]

Therefore

\[
\boxed{
p\mid n
\iff
F_p:S_{np}\longrightarrow S_n
\text{ is an unbranched regular degree-}p\text{ cover}.
}
\]

If \(p\nmid n\), the full preimage surface instead has *both* the old shell and the new shell punctured:

\[
\widehat{\mathbb C}\setminus
\bigl(\{0,\infty\}\cup\mu_n^*\cup\mu_{np}^*\bigr)
\longrightarrow S_n.
\]

So the geometry distinguishes exactly:

\[
\boxed{
\text{raise the exponent of an existing prime}
\longrightarrow
\text{true cyclic cover},
}
\]

whereas

\[
\boxed{
\text{introduce a new prime factor}
\longrightarrow
\text{topology-changing extra old-shell punctures}.
}
\]

Gauss–Bonnet makes the same dichotomy visible in area. Since

\[
\operatorname{Area}(S_n)=2\pi\varphi(n),
\]

we have

\[
\varphi(np)=
\begin{cases}
p\varphi(n),&p\mid n,\\
(p-1)\varphi(n),&p\nmid n.
\end{cases}
\]

Only the first case has the degree-\(p\) area scaling required by a hyperbolic cover. In the second case the missing area

\[
2\pi\varphi(n)
\]

is exactly the topological cost of the inherited shell that must also be removed in the true preimage.

## 4. Why this is not yet an RH mechanism

The equivalence

\[
n\text{ prime}\iff\mu_n=\{1\}\sqcup\mu_n^*
\]

is elementary, so merely rephrasing it as a cover does not solve a hard arithmetic problem. Likewise, using only the area recovers \(\varphi(n)\) and is not new information.

The possible new direction is the **nonlinear geometry of the covering defect** for composite levels. For every \(n\), let

\[
Y_n:=F_n^{-1}(B)
=
\widehat{\mathbb C}\setminus(\{0,\infty\}\cup\mu_n),
\]

so \(Y_n\subseteq X_n^{\mathrm{birth}}\), with equality exactly for prime \(n\). If \(\rho_{Y_n}|dz|\) and \(\rho_{X_n}|dz|\) are their complete Poincare metrics, define on \(Y_n\)

\[
\mathcal D_n(z)
:=
\log\frac{\rho_{Y_n}(z)}{\rho_{X_n}(z)}.
\]

Domain monotonicity gives

\[
\mathcal D_n\ge0,
\]

and strict Schwarz–Pick rigidity gives

\[
\boxed{\mathcal D_n\equiv0\iff n\text{ is prime}.}
\]

Away from punctures the two curvature \(-1\) metrics satisfy Liouville's equation, hence

\[
\boxed{
\Delta\mathcal D_n
=
\rho_{X_n}^2\bigl(e^{2\mathcal D_n}-1\bigr).
}
\]

At an inherited root, \(Y_n\) has a cusp while \(X_n^{\mathrm{birth}}\) is smooth, so \(\mathcal D_n\to+\infty\). At punctures shared by both surfaces the leading cusp singularity is the same. Inversion \(z\mapsto1/\bar z\), which is equatorial reflection in PC-015, preserves both domains and therefore preserves \(\mathcal D_n\).

This defect field is a canonical nonlinear two-dimensional object. It should be investigated before defining any scalar zeta/determinant from it. A scalar aggregate chosen merely to detect \(\mathcal D_n=0\) would only be a dressed-up primality test.

## Literature / novelty check

- The full-root power-map covers are classical. Recent work of Bishop–Rempe gives closely related root-of-unity punctured-sphere constructions using rational power maps, so no novelty is claimed for full-root cyclic covers.
- The thrice-punctured sphere and finite cyclic covers are standard objects in Fuchsian/uniformization theory.
- Venkov–Zograf factorization of Selberg zeta and automorphic scattering determinants for finite-index Fuchsian subgroups is classical.
- Directed searches for primitive-root/new-vertex punctured spheres did not locate the exact equivalence above or the old-prime/new-prime covering dichotomy stated in this form. Because the proof is elementary once the surfaces are defined, historical novelty should still be claimed conservatively.

## Research gate

The candidate becomes mathematically substantive for RH only if the nonlinear family \(\mathcal D_n\), or the cover-versus-surgery category generated by the maps \(z\mapsto z^p\), produces an invariant/dynamics that is not reducible to \(\varphi\), divisibility indicators, Ramanujan sums, Farey discrepancy, or Bost–Connes data.
