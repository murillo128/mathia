# PF-292 — fixed physical high-pass forces a diverging local-frequency floor

**Status:** `EXACT-DERIVED + RELLICH-COMPACTNESS + NEGATIVE/ROUTE-NARROWING`.

PF-291 proves that the fixed PF-227 physical low band becomes complete on every fixed pant window as the cuff length tends to infinity. Equivalently, if `V_n` is the fixed-window source-profile space left after requiring orthogonality to all physical Fourier frequencies `|2\pi k/L_n|\le\kappa`, then the orthogonal projections `P_{V_n}` converge strongly to zero on `L^2(I)`.

That statement has a sharper local consequence. Although the physical cutoff `\kappa` itself is fixed, a unit profile in `V_n\cap H_0^1(I)` cannot remain at bounded **local** Sobolev frequency. Its Dirichlet Rayleigh quotient must diverge uniformly over the whole admissible space. Thus PF-227's fixed-window high witnesses become progressively more oscillatory in the local window even though the global physical cutoff never moves.

More generally, there is a deterministic local frequency scale `R_n\to\infty` such that the PF-291 high projection is asymptotically blind to everything below `R_n`. Consequently a positive PF-290 local shorting deficit can survive only if the normalized mixed-response Riesz representatives themselves develop non-vanishing mass above a diverging local tangential frequency, or fail even a uniform `L^2` amplitude bound. In particular, **any uniform positive fractional Sobolev regularity of the actual normalized response family closes the PF-290 local noncompactness falsifier**.

This does not prove compactness of the full heavy extension angle. It removes another vague escape hatch from PF-291: “the full two-dimensional DtN response” is not enough by itself. To sustain the local obstruction, that response must generate genuinely finer tangential structure on the fixed window, not merely a bounded family of smooth two-dimensional response profiles.

## Claim

Fix the PF-226/PF-227 window

\[
I=(-T,T)
\]

and a physical cutoff `\kappa>0`. Let `L_n\to\infty` and define, exactly as in PF-291,

\[
\Xi_n
=
\left\{\frac{2\pi k}{L_n}:k\in\mathbb Z,
\ \left|\frac{2\pi k}{L_n}\right|\le\kappa\right\},
\]

\[
E_n
=\operatorname{span}\{e^{i\xi t}|_I:\xi\in\Xi_n\},
\qquad
V_n=E_n^\perp\subset L^2(I).
\tag{1}
\]

Let

\[
A_D=-\partial_t^2
\]

be the Dirichlet Laplacian on `I`, and put `K_D=A_D^{1/2}`. Define the constrained local-frequency floor

\[
\omega_n
:=
\inf\left\{
\|K_D\phi\|_2:
\phi\in V_n\cap H_0^1(I),\ \|\phi\|_2=1
\right\}.
\tag{2}
\]

Then

\[
\boxed{\omega_n\longrightarrow\infty.}
\tag{3}
\]

For PF-227's doubly-high witness space `S_n^{\mathrm{hh}}`, every nonzero source profile therefore satisfies

\[
\boxed{
\frac{\|\phi'\|_2}{\|\phi\|_2}
\ge\omega_n\longrightarrow\infty.
}
\tag{4}
\]

At the same time PF-226's construction gives

\[
\|\phi'\|_2\le C\frac{\eta}{s_n}\|\phi\|_2
\qquad(\phi\in S_n),
\tag{5}
\]

and PF-227 guarantees `S_n^{\mathrm{hh}}\ne\{0\}` after a finite head. Hence

\[
\boxed{
1\ll\omega_n\lesssim s_n^{-1}.
}
\tag{6}
\]

The lower divergence in (6) is qualitative; no rate in `L_n` is claimed.

There is also a moving spectral-cut form of the same fact. Let

\[
Q_R=\mathbf1_{[0,R]}(K_D).
\tag{7}
\]

Then one can choose a deterministic sequence `R_n\to\infty` such that

\[
\boxed{
\varepsilon_n:=\|P_{V_n}Q_{R_n}\|\longrightarrow0.
}
\tag{8}
\]

Therefore every `g_n\in L^2(I)` obeys

\[
\boxed{
\|P_{V_n}g_n\|_2
\le
\varepsilon_n\|g_n\|_2
+
\|\mathbf1_{(R_n,\infty)}(K_D)g_n\|_2.
}
\tag{9}
\]

In particular, if for some fixed `\sigma>0`

\[
\sup_n\bigl(
\|g_n\|_2+
\|K_D^\sigma g_n\|_2
\bigr)<\infty,
\tag{10}
\]

then

\[
\boxed{\|P_{V_n}g_n\|_2\longrightarrow0,}
\tag{11}
\]

because

\[
\|\mathbf1_{(R_n,\infty)}(K_D)g_n\|_2
\le R_n^{-\sigma}\|K_D^\sigma g_n\|_2.
\tag{12}
\]

The same statements hold componentwise on the two-window direct-sum profile space used by PF-291.

### PF-290 consequence

Let `G_{n,r}` denote PF-291's fixed-window Riesz representative of the normalized mixed functional relevant to the PF-290 deficit, after the scalar energy scales already isolated there have been removed. PF-291 shows that the PF-227 source high condition places every admissible source profile in `V_n`; the target high condition and PF-290 coercive cut only shrink the admissible set.

Hence, if the direct-sum family `G_{n,r}` is uniformly bounded in `\operatorname{Dom}(K_D^\sigma)` for **any** fixed `\sigma>0`, then the optimized PF-290 local low/high pairing tends to zero and therefore

\[
\boxed{\delta_{n,r}\longrightarrow0}
\tag{13}
\]

for this local witness mechanism.

Conversely, suppose along a tail subsequence the normalized representatives stay bounded in `L^2` while the PF-290 deficit has a positive limsup. Then (9) forces a positive amount of response mass above the diverging local threshold `R_n` along a further subsequence. Thus a persistent local heavy angle requires genuine tangential frequency escape. If the `L^2` norms of the normalized representatives themselves are unbounded, that is a separate amplitude/normalization escape and must be established explicitly; it is not supplied by the smooth fixed-width profile mechanism ruled out by PF-291.

## 1. Strong annihilation plus Rellich compactness forces the local frequency floor to diverge

PF-291 proves

\[
P_{V_n}\longrightarrow0
\qquad\text{strongly on }L^2(I).
\tag{14}
\]

Assume (3) is false. Then there are a subsequence, still denoted by `n`, and unit vectors

\[
\phi_n\in V_n\cap H_0^1(I)
\]

with

\[
\|\phi_n'\|_2\le C.
\tag{15}
\]

The unit `L^2` norm and (15) make `\{\phi_n\}` bounded in `H_0^1(I)`. The classical Rellich compact embedding on a bounded interval therefore gives a further subsequence and `\phi\in L^2(I)` such that

\[
\phi_n\to\phi
\qquad\text{strongly in }L^2(I).
\tag{16}
\]

But `P_{V_n}\phi_n=\phi_n`, so

\[
\begin{aligned}
1=\|\phi_n\|_2
&=\|P_{V_n}\phi_n\|_2\\
&\le
\|P_{V_n}(\phi_n-\phi)\|_2
+
\|P_{V_n}\phi\|_2\\
&\le
\|\phi_n-\phi\|_2
+
\|P_{V_n}\phi\|_2
\longrightarrow0,
\end{aligned}
\tag{17}
\]

where the last term vanishes by (14). This contradiction proves (3).

Equation (4) is immediate from PF-291's exact equivalence between PF-227 source-highness and membership in `V_n`. Equation (5) is PF-226's fixed-window band bound, so any nonzero PF-227 high witness gives the upper estimate in (6).

The key point is conceptual: the global physical threshold stays fixed, but the **support restriction to a fixed window** and the densifying global low-frequency grid together force an emergent local threshold that goes to infinity.

## 2. Finite local spectral sectors are annihilated in operator norm

For fixed `R`, `Q_R` has finite rank. Strong convergence (14), together with `\|P_{V_n}\|\le1`, is therefore uniform on the compact unit sphere of `\operatorname{Ran}Q_R`:

\[
\boxed{
\|P_{V_n}Q_R\|\longrightarrow0
\qquad(R\text{ fixed}).
}
\tag{18}
\]

Choose integers `m=1,2,\ldots`. For each `m`, select `N_m` so large that

\[
n\ge N_m
\quad\Longrightarrow\quad
\|P_{V_n}Q_m\|\le m^{-1}.
\tag{19}
\]

Take the `N_m` increasing and define `R_n=m` for

\[
N_m\le n<N_{m+1}.
\]

Then `R_n\to\infty` and (8) follows. Decomposing

\[
g_n=Q_{R_n}g_n+(I-Q_{R_n})g_n
\]

and using `\|P_{V_n}\|\le1` gives (9). Spectral calculus gives (12), hence (10) implies (11).

No explicit growth rate for `R_n` is asserted. PF-291 already warns that approximation by the fixed physical band can be extremely ill-conditioned on a finite window. The new statement spends only compactness and therefore deliberately keeps the scale qualitative.

## 3. What remains of the local heavy-angle obstruction

PF-291 already rules out a fixed precompact scalar response profile such as the exact normalized reciprocal-width family. Equations (8)--(13) sharpen the surviving alternative.

A local positive PF-290 deficit cannot be sustained by a normalized response family with any uniform positive amount of local Sobolev regularity. The response must instead transport a non-negligible fraction of its `L^2` mass to tangential frequencies beyond a threshold that itself diverges with the pant index, or else its normalized `L^2` amplitude must lose control.

This separates the plausible mechanisms listed after PF-291:

- a fixed smooth variable-width multiplier is closed already by PF-291;
- any uniformly positive-Sobolev fixed-window DtN response is closed by the present finding;
- a genuine survivor must exhibit increasing tangential oscillation, mass migration outside every fixed central window, an amplitude/normalization blow-up, or a nonlocal/global coupling not represented by the fixed-window Riesz family.

The immediate positive test is therefore much cheaper than a full weak-trace estimate: prove **any** uniform bound

\[
\sup_{n,r}\|K_D^\sigma G_{n,r}\|_2<\infty
\qquad\text{for one }\sigma>0
\tag{20}
\]

for the actual energy-normalized mixed response on the fixed PF-226/PF-227 window. Such a bound would close the PF-289/PF-290 local noncompactness mechanism outright. Failure of every such bound would identify the precise fine-scale response that must be understood before returning to global heavy-range counting.

## Prior-art and novelty audit

The compactness input is classical. F. Rellich, *Ein Satz über mittlere Konvergenz*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse (1930), 30--35, is the original `L^2` compactness source behind the bounded-interval embedding used in (16). The facts that strong convergence is uniform on a fixed finite-dimensional unit sphere and that spectral tails of `K_D^\sigma` obey (12) are elementary Hilbert-space/spectral-theorem consequences. No novelty is claimed for Rellich compactness, finite-rank uniformity, or Sobolev spectral tails.

The project-specific deduction is the combination of PF-291's **densifying fixed physical low grid** with PF-226/PF-227's **fixed-window high witness construction**. It converts a cutoff that is globally fixed in physical frequency into a local Sobolev-frequency floor `\omega_n\to\infty`, and then converts the PF-290 persistence question into a necessary moving-frequency escape condition for the actual mixed response. The exponential-system literature studies completeness, frames, interpolation, and density in much greater generality; this finding does not claim a new theorem in that literature.

## Boundaries and falsification

This finding is local to the fixed PF-226/PF-227 window. It does not apply unchanged to a window growing with `n`, and it gives no explicit rate for `\omega_n` or `R_n`.

It also does not prove that the actual mixed response has any positive Sobolev bound. PF-245 shows that the raw actual seam square root has a critical complex-frequency branch obstruction, and PF-255--PF-256 control only specific geometric transports through two derivatives. Those results make the regularity test concrete but do not by themselves establish (20) for the complete mixed Riesz representative.

A direct falsification would be a normalized sequence `\phi_n\in V_n\cap H_0^1(I)` with uniformly bounded `\|\phi_n'\|_2`, contradicting (3), or a failure of PF-291's strong convergence (14). At the project level, a persistent PF-290 deficit together with a verified uniform positive-Sobolev bound for the exact normalized response would contradict the present reduction.

No compactness or weak-`S_1` theorem for the full heavy angle, no scattering/determinant statement, no zeta-zero correspondence, no critical-line statement, and no RH consequence is established.