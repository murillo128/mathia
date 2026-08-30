# WP-046 — shell-dependent radial Schur speeds still cancel the boundary Weil birth term

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the bounded shell-dependent finite-radial escape left open by `WP-045`. Allowing each primitive shell to approach the Prime-Circle radial boundary at its own positive speed gives a much larger positive Gram family than the shell-blind construction of `WP-044`/`WP-045`. Nevertheless, on every fixed finite shell space its boundary blocks still have the form

\[
L_\varepsilon I + C + B_{ij}+o(1),
\]

where `C` is the same Prime-Circle Weil birth operator in every radial block and the new shell dependence is confined to diagonal operators `B_ij`. Eliminating a radial channel by an ordinary positive Schur/Feshbach map cancels the whole common operator `L_epsilon I+C` from the leading response **without requiring `B_ij` to commute with `C`**. The boundary Schur limit is a direct sum, over arithmetic shells, of universal positive radial conditional-covariance kernels and has no cross-shell arithmetic entries. Thus merely making the radial approach conductor/shell dependent does not rescue the finite Weil term while retaining positivity.

This result does **not** rule out a deformation that changes the leading cross-shell feature geometry itself, singular cutoff-dependent speeds, non-comparable boundary scales, an infinite-dimensional nonseparable finite--archimedean sector, or a renormalized subleading response with a new independent sign theorem. It rules out the natural proposal that shell-dependent radial clocks, followed by the same canonical positive Gram and Schur machinery, are already enough.

## 1. The shell-dependent deformation remains an unconditional positive Gram

Fix a finite primitive-shell set `S`, and let

\[
E=\mathbb C^S.
\]

The exact primitive Prime-Circle radial Gram of `WP-036` is

\[
\widehat G_x
=\sum_{r\ge1}\frac{x^r}{r}u_ru_r^*,
\qquad
(u_r)_n=\frac{c_n(r)}{\sqrt{\varphi(n)}}.
\tag{1}
\]

`WP-044` polarized one common radius per radial channel. To test the shell-dependent escape as generously as possible, assign instead a radius to every pair `(radial channel, shell)`:

\[
0<x_{i,n}<1,
\qquad i=1,\ldots,k,
\qquad n\in S.
\tag{2}
\]

Define feature coordinates

\[
\Phi_{i,n}(r)
:=\frac{x_{i,n}^{r/2}}{\sqrt r}\,(u_r)_n.
\tag{3}
\]

Their Gram matrix, indexed by `(i,m)` and `(j,n)`, is

\[
\boxed{
\mathbb K_{ij}(m,n)
=\sum_{r\ge1}\frac{(x_{i,m}x_{j,n})^{r/2}}r
(u_r)_m(u_r)_n
=\widehat G_{\sqrt{x_{i,m}x_{j,n}}}(m,n).
}
\tag{4}
\]

Hence

\[
\boxed{\mathbb K\succeq0}
\tag{5}
\]

for **arbitrary** shell-dependent radii. No arithmetic sign theorem has been inserted: positivity is simply the Hilbert-space Gram theorem for the actual Ramanujan feature system.

This family strictly contains the shell-blind polarization of `WP-044`, recovered when `x_{i,n}=x_i` for all `n`.

## 2. Comparable shell-dependent boundary speeds change only the diagonal finite part

Let every shell approach the boundary at an arbitrary fixed positive speed,

\[
x_{i,n}(\varepsilon)
=1-c_{i,n}\varepsilon+o(\varepsilon),
\qquad
c_{i,n}>0,
\qquad
\varepsilon\downarrow0.
\tag{6}
\]

Because both the shell set and radial channel set are finite, all `c_{i,n}` are automatically bounded above and away from zero after fixing the data.

For a pair `(m,n)`, equation (4) is exactly one matrix entry of the ordinary radial Gram evaluated at the pair-dependent scalar radius

\[
z_{ij;mn}
=\sqrt{x_{i,m}x_{j,n}}.
\tag{7}
\]

`WP-034` gives, entrywise on every fixed shell box,

\[
\widehat G_z(m,n)
=L(z)\delta_{mn}+C_{mn}+o(1),
\qquad
L(z)=-\log(1-z),
\qquad z\to1^-.
\tag{8}
\]

For `m=n`, equation (6) gives

\[
1-z_{ij;nn}
=\frac{c_{i,n}+c_{j,n}}2\varepsilon+o(\varepsilon),
\tag{9}
\]

and therefore

\[
L(z_{ij;nn})
=L_\varepsilon
-\log\frac{c_{i,n}+c_{j,n}}2
+o(1),
\qquad
L_\varepsilon:=-\log\varepsilon.
\tag{10}
\]

For `m\ne n`, the collision term in (8) is absent and the entry simply tends to `C_mn`. Since there are only finitely many entries, the remainders are uniform in operator norm. Thus each radial block has the exact asymptotic form

\[
\boxed{
\mathbb K_{ij}
=X_\varepsilon+B_{ij}+o(1),
\qquad
X_\varepsilon:=L_\varepsilon I_E+C,
}
\tag{11}
\]

where `B_ij` is the shell-diagonal operator

\[
\boxed{
(B_{ij})_{nn}
=-\log\frac{c_{i,n}+c_{j,n}}2.
}
\tag{12}
\]

The crucial structural fact survives arbitrary shell-dependent speeds: **the same full shell operator `X_epsilon=L_epsilon I+C` occurs in every radial block**. Shell dependence changes only an additional diagonal `O(1)` term.

## 3. Schur elimination cancels the common operator even without commutativity

Choose one radial channel `k` to eliminate. Since `E` is finite dimensional and `L_epsilon->infinity`, the diagonal block

\[
\mathbb K_{kk}
=X_\varepsilon+B_{kk}+o(1)
\tag{13}
\]

is strictly positive and invertible for sufficiently small `epsilon`, with inverse norm `O(L_epsilon^{-1})`.

The positive Schur/Feshbach response on the retained channels is

\[
\mathcal S^{(k)}_{ij}
:=
\mathbb K_{ij}
-\mathbb K_{ik}\mathbb K_{kk}^{-1}\mathbb K_{kj},
\qquad i,j\ne k.
\tag{14}
\]

Because the parent matrix (5) is positive,

\[
\boxed{\mathcal S^{(k)}\succeq0.}
\tag{15}
\]

The shell-dependent operators `B_ij` generally do **not** commute with the arithmetic matrix `C`. So the commuting scalar-block calculation of `WP-045` is not enough by itself. Nevertheless, the required cancellation is purely algebraic and survives noncommutativity.

Ignore the `o(1)` remainders for one exact step and put

\[
Y_\varepsilon:=X_\varepsilon+B_{kk},
\qquad
\Delta_i:=B_{ik}-B_{kk},
\qquad
\Gamma_j:=B_{kj}-B_{kk}.
\tag{16}
\]

Then

\[
X_\varepsilon+B_{ik}=Y_\varepsilon+\Delta_i,
\qquad
X_\varepsilon+B_{kj}=Y_\varepsilon+\Gamma_j.
\]

Associativity alone gives

\[
\begin{aligned}
&(Y_\varepsilon+\Delta_i)
Y_\varepsilon^{-1}
(Y_\varepsilon+\Gamma_j)
\\
&\qquad
=Y_\varepsilon+\Delta_i+\Gamma_j
+\Delta_iY_\varepsilon^{-1}\Gamma_j.
\end{aligned}
\tag{17}
\]

No pair of the displayed operators has been commuted. Consequently

\[
\boxed{
\begin{aligned}
&(X_\varepsilon+B_{ij})
-(X_\varepsilon+B_{ik})
(X_\varepsilon+B_{kk})^{-1}
(X_\varepsilon+B_{kj})
\\
&\quad=
D^{(k)}_{ij}
-\Delta_iY_\varepsilon^{-1}\Gamma_j,
\end{aligned}
}
\tag{18}
\]

with

\[
\boxed{
D^{(k)}_{ij}
=B_{ij}-B_{ik}-B_{kj}+B_{kk}.
}
\tag{19}
\]

The whole common operator `X_epsilon`, including the non-diagonal arithmetic matrix `C`, has disappeared from the `O(1)` term.

Restoring the `o(1)` remainders in (11) changes the Schur response by `o(1)`: the cross blocks have norm `O(L_epsilon)`, the eliminated inverse has norm `O(L_epsilon^{-1})`, and the resolvent perturbation from the diagonal `o(1)` term has norm `o(L_epsilon^{-2})`. Meanwhile

\[
\|\Delta_iY_\varepsilon^{-1}\Gamma_j\|
=O(L_\varepsilon^{-1}).
\tag{20}
\]

Therefore

\[
\boxed{
\mathcal S^{(k)}_{ij}(\varepsilon)
=D^{(k)}_{ij}+o(1),
}
\tag{21}
\]

and hence

\[
\boxed{
\mathcal S^{(k)}(\varepsilon)
\longrightarrow D^{(k)}
}
\tag{22}
\]

in operator norm on every fixed finite shell space.

## 4. The boundary response is positive but shell-diagonal

Each `B_ij` is diagonal in the primitive-shell basis, so every `D_ij^(k)` is diagonal as well. Fix one shell `n` and abbreviate

\[
c_i=c_{i,n}.
\]

The scalar radial block on that shell is

\[
B_{ij}(n)=-\log\frac{c_i+c_j}{2}.
\tag{23}
\]

Equation (19) becomes

\[
\boxed{
D^{(k)}_{ij}(n)
=
-\log\frac{c_i+c_j}{2}
+\log\frac{c_i+c_k}{2}
+\log\frac{c_k+c_j}{2}
-\log c_k.
}
\tag{24}
\]

As in `WP-045`, the elementary logarithm integral gives

\[
\boxed{
D^{(k)}_{ij}(n)
=
\int_0^\infty
\frac{
(e^{-c_it/2}-e^{-c_kt/2})
(e^{-c_jt/2}-e^{-c_kt/2})
}{t}\,dt.
}
\tag{25}
\]

Thus for each shell `n`, the radial matrix `[D_ij^(k)(n)]` is positive semidefinite. The full limit is their orthogonal direct sum:

\[
\boxed{
D^{(k)}
=\bigoplus_{n\in S}D^{(k)}(n)
\succeq0.
}
\tag{26}
\]

So the hoped-for sign theorem survives perfectly. What survives with it is only a **shell-diagonal conditional-covariance response**. For distinct primitive shells `m\ne n`,

\[
\boxed{
D^{(k)}_{ij}(m,n)=0.
}
\tag{27}
\]

The cross-shell Prime-Circle birth coefficients, including the interior ray values

\[
C_{dp^a,d}
=-\frac{\log p}{p^{a/2}},
\tag{28}
\]

are absent from the boundary Schur limit.

## 5. Making the radial clock depend on conductor does not create finite--archimedean coupling

A particularly natural attempted repair after `WP-045` is to choose the speeds from an intrinsic shell statistic, for example conductor/order, totient, or another Prime-Circle scale, so that the radial elimination is no longer shell blind.

Equations (11)--(27) show exactly what such a choice can do at leading order. It changes

\[
B_{ij}(n)
=-\log\frac{c_{i,n}+c_{j,n}}2
\]

and therefore changes the positive radial metric separately on each shell. It cannot create an `O(1)` interaction between two different shells because all cross-shell information remains locked in the common matrix `C`, which Schur elimination cancels.

This matters especially for the `WP-036` same-parent bridge. Its `q=2` Mellin diagonal contains the Riemann `psi(s/2)` scale, while its boundary finite part contains `C`. A shell-dependent choice of boundary speed may encode `q`, conductor, or another local label in the radial diagonal response, but ordinary finite Schur elimination still produces

\[
\text{positive radial response depending on shell }n
\quad\oplus\quad
\text{no cross-shell }C.
\]

Thus **shell-dependent radial clocks are not the missing nonseparable finite--archimedean coupling**. To survive this obstruction, nonseparability must enter the leading feature geometry or pairing itself, not only the rate at which existing shell coordinates approach the same boundary.

## 6. Where the arithmetic goes: only a vanishing resolvent correction

Equation (18) also locates the missing arithmetic information. It survives only through

\[
-\Delta_i
(L_\varepsilon I+C+B_{kk})^{-1}
\Gamma_j,
\tag{29}
\]

whose norm is `O(1/L_epsilon)`.

In the idealized common-mode model, with the unknown `o(1)` boundary remainder deleted, the finite-dimensional Neumann expansion gives

\[
(L_\varepsilon I+C+B_{kk})^{-1}
=
\frac1{L_\varepsilon}I
-\frac1{L_\varepsilon^2}(C+B_{kk})
+O(L_\varepsilon^{-3}).
\tag{30}
\]

Hence the arithmetic matrix first reappears only at the **second subleading resolvent order**:

\[
\begin{aligned}
\mathcal S^{(k),\mathrm{ideal}}_{ij}
&=D^{(k)}_{ij}
-\frac1{L_\varepsilon}\Delta_i\Gamma_j
\\
&\quad
+\frac1{L_\varepsilon^2}
\Delta_i(C+B_{kk})\Gamma_j
+O(L_\varepsilon^{-3}).
\end{aligned}
\tag{31}
\]

This does not produce a new positive Weil form. Isolating the `C` coefficient would require subtracting the positive `O(1)` limit, subtracting the shell-diagonal `1/L_epsilon` term, and multiplying the remainder by `L_epsilon^2`. Positivity of the original Schur response supplies no sign theorem for that renormalized coefficient.

Equation (31) is deliberately **not** asserted as an asymptotic expansion of the exact Prime-Circle response: the presently established boundary error is only `o(1)` and can dominate `L_epsilon^{-1}` or `L_epsilon^{-2}`. It is a diagnostic of the exact ideal common-mode algebra. Any attempt to exploit the subleading resolvent must first prove sharper radial asymptotics and then prove a new sign theorem after the singular renormalization.

## 7. Matched control: the cancellation is completely arithmetic-blind

The core calculation does not use any special property of von Mangoldt weights, Ramanujan sums, or primes after equation (11) has been established.

Replace `C` in

\[
X_\varepsilon=L_\varepsilon I+C
\]

by **any** bounded self-adjoint matrix `A` on the finite shell space. Equations (17)--(22) are unchanged. The leading Schur limit is still `D^(k)`, independent of `A`.

Therefore the disappearance of `C` cannot itself encode a hidden Riemann theorem. It is a universal cancellation law for a large common operator shared by all covariance blocks. Prime arithmetic enters only in establishing that the Prime-Circle radial family has precisely this common boundary finite part.

This matched control also prevents a misleading novelty claim: the positivity of Gram matrices, positivity of Schur complements, and the interpretation of Schur complements as conditional covariances are classical linear/Hilbert-space facts. The Mathia-specific statement is the synthesis of those facts with the exact Prime-Circle shell-dependent boundary deformation (4)--(12) and the resulting disappearance of the Weil birth matrix.

## 8. Prior-art and novelty audit

The closest general machinery remains classical Schur/Feshbach or conditional-covariance reduction. The present argument does not claim a new Schur-complement theorem; equation (17) is elementary block algebra, and equation (25) is the same conditionally positive logarithmic radial kernel already exposed in `WP-044`/`WP-045`.

The closest RH/Weil comparison remains Connes--Consani's archimedean compression mechanism already recorded in `SOURCES.md`. There the sign comes from compressing the scaling action to the orthogonal complement of phase-space cutoff projections and controlling the resulting trace with Sonin/prolate/Toeplitz structure. The shell-dependent coordinatewise radial clocks tested here do not reproduce that change of space or pairing, and this no-go does not rule out it or an equivalent semilocal construction.

A literature search for Schur-complement positivity/conditional covariance finds the expected broad matrix-analysis and covariance theory, not an arithmetic result identifying the Prime-Circle boundary cancellation. Conversely, current Weil-positivity compression literature acts on global/semilocal spaces rather than by assigning independent comparable boundary speeds to finitely many primitive shells. The defensible novelty boundary is therefore narrow: **the standard sign-preserving operation fails on this enlarged Mathia-native radial family for an exact structural reason**. No claim of novelty is made for the underlying matrix theorem.

## 9. Boundary of the no-go

This finding rules out the following route on every fixed finite primitive-shell space:

```text
positive Prime-Circle Ramanujan feature Gram
    -> finitely many radial channels
    -> arbitrary fixed positive boundary speed c_(i,n) for every shell
    -> ordinary positive Schur/Feshbach elimination
    -> leading finite boundary response retaining C.
```

It does **not** rule out:

- shell-dependent deformations that alter the `O(1)` **off-diagonal feature coupling** rather than only the radial speed;
- boundary approaches not comparable to one common `epsilon`;
- speeds depending singularly on `epsilon` or on a cofinal shell cutoff;
- exchanging the boundary limit with an infinite shell limit;
- an infinite-dimensional radial/archimedean sector;
- a subleading extraction after proving stronger asymptotics, provided an independent sign theorem survives the required subtraction/rescaling;
- nonlinear determinant/intersection constructions, gradings, cohomology, or relative-order pairings not reducible to this Schur response.

The fixed finite-shell hypothesis is essential. It is what makes the entrywise `o(1)` boundary expansion uniform in operator norm and keeps `C` bounded while `L_epsilon` diverges.

## 10. Exact falsification tests

The claim is killed by any one of the following:

1. a shell-dependent feature Gram of the precise form (3)--(4) for which the boundary block expansion (11)--(12) fails on a fixed finite shell set;
2. a failure of the noncommutative algebraic identity (17)--(19);
3. an ordinary Schur complement of (11) whose `O(1)` boundary limit retains a nonzero cross-shell entry of `C`;
4. a shell `n` and radial speeds for which the matrix in (24) has a negative direction, contradicting the Gram integral (25);
5. evidence that the shell-dependent speed deformation tested here is already equivalent, under a sign-preserving change of variables, to a known global Weil-positive compression such as the Connes--Consani/Sonin mechanism.

Absent such a failure, shell-dependent radial speeds close one of the most immediate finite-dimensional escapes from `WP-045` without narrowing the genuinely different possibilities listed in Section 9.
