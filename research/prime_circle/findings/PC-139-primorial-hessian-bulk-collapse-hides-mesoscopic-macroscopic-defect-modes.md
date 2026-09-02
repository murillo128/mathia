# PC-139 — primorial Hessian bulk collapse hides mesoscopic macroscopic defect modes

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-SIEVE-BOUNDARY` + `SURVIVING-MECHANISM`. PC-136 proved that the canonical cross-shell-only resultant Hessian on primorial common refinements has the same normalized bulk spectral law as the full inverse-square polygon, with Wasserstein defect `Theta((log x)^-2)`. PC-138 then proved that the absolute top eigenpair of the cross-shell operator itself is exactly universal at every even level. Those facts leave open whether the omitted within-shell operator actually becomes small, or whether the bulk convergence hides a vanishing fraction of order-`N^2` modes.

The second possibility is forced. Along the primorials `N_x=prod_{p<=x}p`, the defect

\[
D_{N_x}:=L_{N_x}-H_{N_x}^{\times}
=\bigoplus_{d\mid N_x}L_d^{\rm int}
\]

has a **mesoscopic macroscopic spectral tail**: for every fixed `0<alpha<1/(8 pi^2)`, the number of eigenvalues of `D_{N_x}` at least `alpha N_x^2` is

\[
\boxed{\Theta\!\left(\frac{N_x}{(\log x)^2}\right).}
\]

A canonical subspace giving the lower bound comes from gap-two pairs inside the primitive shell. Its exact dimension is

\[
E_x=\prod_{3\le p\le x}(p-2),
\]

and its arithmetic normalization is

\[
\boxed{
\frac{E_x}{N_x}
=2C_{2,x}\left(\frac{\varphi(N_x)}{N_x}\right)^2,
\qquad
C_{2,x}:=\prod_{3\le p\le x}
\frac{p(p-2)}{(p-1)^2}.
}
\]

Thus the surviving edge-mode multiplicity is not a new RH alphabet: its forced arithmetic scale is exactly the finite twin-prime singular factor times the same squared primorial totient product that PC-137 already classicalized to Nicolas/Mertens. What remains genuinely open is the detailed placement and organization of the non-universal edge modes beyond this guaranteed short-chord subspace.

## 1. The PC-136 defect contains the primitive-shell internal Laplacian

For every `N`, PC-136 gives

\[
L_N-H_N^{\times}=D_N
=\bigoplus_{d\mid N}L_d^{\rm int}\succeq0,
\]

where `L_d^int` contains exactly the inverse-square chord edges whose endpoints belong to the same exact-order shell `S_d`.

At the top shell,

\[
S_N=\{a\bmod N:(a,N)=1\}=U(N),
\]

so every pair of reduced residues contributes an edge to the primitive block of `D_N`. If two residues differ by `2`, their edge weight is

\[
w_2(N)
=\frac1{4\sin^2(2\pi/N)}.
\]

The associated two-vertex Laplacian has its nonzero eigenvalue

\[
\boxed{
\beta_N:=2w_2(N)
=\frac1{2\sin^2(2\pi/N)}.
}
\]

After the natural `N^2` normalization,

\[
\boxed{
\frac{\beta_N}{N^2}
\longrightarrow\frac1{8\pi^2}.
}
\]

So a linear number of disjoint gap-two primitive pairs would immediately force a macroscopic spectral tail. The primorial reduced-residue geometry supplies a mesoscopic, rather than linear, number of exactly such pairs.

## 2. Gap-two primitive pairs are an exact matching

Assume `x>=3` and put

\[
N_x=\prod_{p\le x}p.
\]

Define the cyclic gap-two edge set

\[
\mathcal E_x
:=\bigl\{\{a,a+2\}:a,a+2\in U(N_x)\bigr\},
\]

with arithmetic modulo `N_x`. Since `N_x>4`, the parametrization by the starting point `a` does not double-count an unoriented edge.

CRT counts the allowed starts independently prime by prime. Modulo `2`, there is one allowed class. For each odd `p|N_x`, the conditions

\[
a\not\equiv0,-2\pmod p
\]

leave exactly `p-2` classes. Hence

\[
\boxed{
|\mathcal E_x|=E_x
=\prod_{3\le p\le x}(p-2).
}
\]

More is true: these edges are pairwise vertex-disjoint. Because `3|N_x`, if both `a` and `a+2` are units, then modulo `3` they must be the two nonzero classes. Consequently

\[
a-2\equiv0\pmod3,
\qquad
a+4\equiv0\pmod3,
\]

so neither endpoint can belong to a second gap-two unit pair. Thus `mathcal E_x` is an **exact matching** inside the primitive shell.

This is an important distinction from an appeal to a conjectural twin-prime pattern. No primality assertion is present: the count is a finite CRT identity for reduced residues modulo the primorial.

## 3. Min-max forces `E_x` order-`N_x^2` defect eigenvalues

For each edge `e={a,a+2}` in `mathcal E_x`, let

\[
v_e=e_a-e_{a+2}.
\]

Because the selected edges form a matching, the vectors `{v_e}` have disjoint supports and are mutually orthogonal. Let

\[
V_x:=\operatorname{span}\{v_e:e\in\mathcal E_x\},
\qquad
\dim V_x=E_x.
\]

For

\[
v=\sum_{e\in\mathcal E_x}c_ev_e,
\]

the selected gap-two edges alone contribute

\[
\langle v,D_{N_x}v\rangle
\ge
4w_2(N_x)\sum_e|c_e|^2,
\]

while

\[
\|v\|^2=2\sum_e|c_e|^2.
\]

Therefore every nonzero vector in `V_x` satisfies

\[
\frac{\langle v,D_{N_x}v\rangle}{\|v\|^2}
\ge
2w_2(N_x)=\beta_{N_x}.
\]

Courant--Fischer now gives the exact counting lower bound

\[
\boxed{
\#\{j:\lambda_j(D_{N_x})\ge\beta_{N_x}\}
\ge E_x.
}
\]

In particular,

\[
\boxed{
\liminf_{x\to\infty}
\frac{\|D_{N_x}\|}{N_x^2}
\ge\frac1{8\pi^2}>0.
}
\]

So the PC-136 bulk collapse is emphatically **not** operator-norm convergence. The within-shell defect remains macroscopically large on a growing family of directions even though that family occupies a vanishing fraction of the `N_x`-dimensional space.

## 4. The macroscopic tail has the exact mesoscopic scale `N_x/(log x)^2`

Let

\[
M_x(\alpha)
:=\#\{j:\lambda_j(D_{N_x})\ge\alpha N_x^2\}.
\]

For every fixed

\[
0<\alpha<\frac1{8\pi^2},
\]

the previous section gives, for all sufficiently large `x`,

\[
M_x(\alpha)\ge E_x.
\]

The lower count has a classical Euler-product asymptotic. Write

\[
C_{2,x}
:=\prod_{3\le p\le x}
\left(1-\frac1{(p-1)^2}\right)
=\prod_{3\le p\le x}\frac{p(p-2)}{(p-1)^2}.
\]

Then the identity

\[
\frac{E_x}{N_x}
=\frac12\prod_{3\le p\le x}\left(1-\frac2p\right)
\]

factors exactly as

\[
\boxed{
\frac{E_x}{N_x}
=2C_{2,x}
\left(\frac{\varphi(N_x)}{N_x}\right)^2.
}
\]

Since `C_{2,x}->C_2>0` and Mertens gives

\[
\frac{\varphi(N_x)}{N_x}
\sim\frac{e^{-\gamma}}{\log x},
\]

we obtain

\[
\boxed{
E_x
\sim
2C_2e^{-2\gamma}
\frac{N_x}{(\log x)^2}.
}
\]

For the matching upper scale, positivity gives

\[
\alpha N_x^2 M_x(\alpha)
\le\operatorname{tr}D_{N_x}.
\]

PC-136 proved exactly

\[
\operatorname{tr}D_N
=\frac{F(N)-N}{12}
\]

and, on primorials,

\[
\frac{F(N_x)}{N_x^3}
=\prod_{p\le x}
\left(1-\frac2p+\frac2{p^3}\right)
=\Theta((\log x)^{-2}).
\]

Therefore

\[
M_x(\alpha)
=O_\alpha\!\left(\frac{N_x}{(\log x)^2}\right).
\]

Combining both sides yields the promised mesoscopic law

\[
\boxed{
M_x(\alpha)
=\Theta_\alpha\!\left(\frac{N_x}{(\log x)^2}\right)
\qquad
\left(0<\alpha<\frac1{8\pi^2}\right).
}
\]

Thus the defect has three simultaneous scales: macroscopic eigenvalue size `Theta(N_x^2)`, mesoscopic multiplicity `Theta(N_x/log^2 x)`, and vanishing normalized mass `Theta(1/log^2 x)`. This reconciles strong operator non-convergence with PC-136's Wasserstein/bulk convergence.

## 5. RH audit: the forced tail multiplicity classicalizes before any zero mechanism appears

The exact identity

\[
\frac{E_x}{N_x}
=2C_{2,x}\left(\frac{\varphi(N_x)}{N_x}\right)^2
\]

is the key novelty control. The factor `C_{2,x}` is the finite Euler product tending to the classical prime-pair/twin-prime singular constant, while the remaining factor is precisely the squared primorial totient product already isolated in PC-137.

Therefore any RH-equivalent normalization manufactured **solely from the guaranteed short-chord mode count `E_x`**, the known factor `C_{2,x}`, and the conductor `N_x` immediately reduces to the Nicolas/Mertens criterion of PC-137. The prime-circle geometry has given a concrete spectral realization of that scale, but not a new functional equation, spectral parameter, gamma factor, critical-line symmetry, or zero divisor.

This does not classicalize the full edge spectrum. The statement is only a lower-dimensional spectral embedding plus a trace upper bound. The actual values of the non-universal eigenvalues, their eigenvectors after all within-shell edges are included, correlations between different short-gap constellations, the second eigenvalue of `H_{N_x}^times`, and cross-level organization of the mesoscopic tail remain unresolved. Those would require information beyond the scalar count `E_x`.

## 6. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the ingredients. The inverse-square chord kernel and full regular-polygon spectrum are the classical Calogero--Perelomov structure already anchored in `SOURCES.md`. Reduced-residue spacing is a classical analytic-number-theory subject; directed checks included Montgomery--Vaughan's work on the distribution of reduced residues. The product

\[
\prod_{p>2}\frac{p(p-2)}{(p-1)^2}
\]

is the standard prime-pair/twin-prime singular factor from Hardy--Littlewood theory. The min-max inference from an orthogonal family of disjoint weighted edges is standard spectral graph theory.

Directed searches for primitive-root inverse-square Laplacians, reduced-residue `csc^2` spectra, primorial Laplacians, and roots-of-unity Riesz energies did not expose this exact Prime-Circle statement combining the PC-136 defect with the gap-two matching. That absence is not evidence of priority. The durable research contribution is the boundary classification: **the canonical primorial Hessian defect does not become small as an operator; instead its bulk collapse is carried by a classical-sieve-sized mesoscopic family of macroscopic modes.**

The arithmetic leading constant is itself a warning against overclaiming. Its appearance is the local admissibility product for a two-point pattern in a reduced residue system, not evidence for the twin-prime conjecture and not a new route to zeta zeros.

## 7. Falsification surface and consequences

1. For every primorial `N_x` with `x>=3`, direct CRT enumeration must give exactly `E_x=prod_{3<=p<=x}(p-2)` cyclic pairs `a,a+2` with both endpoints in `U(N_x)`.
2. Those pairs must be vertex-disjoint; divisibility by `3` provides the exact local obstruction to a three-term step-two run.
3. For every vector in their difference-vector span, the Rayleigh quotient of `D_{N_x}` must be at least `1/(2 sin^2(2 pi/N_x))`.
4. The resulting eigenvalue-count lower bound must agree with direct diagonalization. Bounded numerical checks at `N=6,30,210` give respectively at least `1,3,15` guaranteed directions; direct spectra satisfy the bound comfortably.
5. The upper `O(N_x/log^2 x)` count uses the exact PC-136 trace and applies at every fixed positive normalized threshold. If the PC-136 trace identity were revised, this upper half would need to be re-audited.
6. Nothing here determines the spectrum of `H_{N_x}^times` below its protected top mode. Since `D_{N_x}` and `L_{N_x}` do not commute in general, macroscopic defect modes cannot be naively converted into ordered eigenvalue shifts of `H_{N_x}^times`.

The main research consequence is therefore two-sided. PC-136's bulk collapse cannot be strengthened to operator-norm collapse, so edge/localized investigations remain mathematically legitimate. But the most canonical guaranteed edge population already carries the classical Hardy--Littlewood local factor times the same Nicolas/Mertens totient scale. A genuinely new RH mechanism would have to use the **organization or dynamics of those modes**, not merely their existence or count.
