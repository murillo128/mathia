# FD-196 — Weighted Fourier duality has a sharp geometric recovery line

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** weighted Fourier duality / fractional-Sobolev phase diagram / geometric recovery boundary
- **Depends on:** FD-002, FD-117, FD-193, FD-194, FD-195
- **Classification:** `EXACT-DERIVED + SHARP-WEIGHTED-ROW-DUALITY + FRACTIONAL-SOBOLEV-TRADEOFF + NEGATIVE/NORM-CHANGE-BOUNDARY`

## Claim

`FD-195` shows that the classical Franel quadratic norm loses a full half power when it is used, by generic one-horizon duality, to recover a geometric quotient witness `M(n)` at a horizon `H=Theta(n^2)`. The loss is not peculiar to the unweighted `L^2` norm. There is an exact weighted Fourier phase diagram, and a pure change of Sobolev weight preserves the same half-power deficit unless one proves genuinely new spectral suppression.

For a Farey horizon `H`, write as in `FD-002/FD-117`

\[
\mathcal B_H(k)
:=
\sum_{d\mid k}d\,M\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad k\ge1.
\tag{1}
\]

Equivalently, if

\[
R_H(x):=D_H(x)-x,
\tag{2}
\]

then for every positive frequency

\[
\widehat R_H(k)
=
\frac{\mathcal B_H(k)}{2\pi i k}.
\tag{3}
\]

Fix `0<=sigma<=1` and a finite band `1<=k<=K`. Define

\[
\mathcal E_{H,\sigma}(K)
:=
\sum_{1\le k\le K}
\frac{|\mathcal B_H(k)|^2}{k^{2\sigma}}
=
4\pi^2
\sum_{1\le k\le K}
 k^{2-2\sigma}|\widehat R_H(k)|^2.
\tag{4}
\]

Thus `sigma=1` is the band-limited classical Franel `L^2` Fourier energy, while `sigma=1/2` is the band-limited homogeneous half-Sobolev energy

\[
\mathcal E_{H,1/2}(K)
=4\pi^2\sum_{k\le K}k|\widehat R_H(k)|^2.
\tag{5}
\]

For every `1<=d<=K`, divisor Möbius inversion gives the exact row

\[
M\!\left(\left\lfloor\frac Hd\right\rfloor\right)
=
\frac1d
\sum_{e\mid d}
\mu(d/e)\,\mathcal B_H(e).
\tag{6}
\]

Weighted Cauchy--Schwarz therefore yields

\[
\boxed{
\left|M\!\left(\left\lfloor\frac Hd\right\rfloor\right)\right|^2
\le
\mathcal R_\sigma(d)\,
\mathcal E_{H,\sigma}(K),
}
\tag{7}
\]

where the row factor is exactly

\[
\boxed{
\mathcal R_\sigma(d)
=
d^{2\sigma-2}
\prod_{p\mid d}(1+p^{-2\sigma}).
}
\tag{8}
\]

The coefficient in (8) is not merely a convenient upper bound: it is the exact squared dual norm of the inversion row (6) in the diagonal data space with norm (4). In that unrestricted weighted band geometry the inequality is sharp.

For every fixed `sigma>=0`,

\[
\prod_{p\mid d}(1+p^{-2\sigma})=d^{o(1)},
\tag{9}
\]

so

\[
\mathcal R_\sigma(d)=d^{2\sigma-2+o(1)}.
\tag{10}
\]

Now fix an integer geometric schedule `H=B^m`, `B>=2`, and retain a complete square-root band

\[
K_H=\min\!\left(H,\lfloor c\sqrt H\rfloor\right),
\qquad c\ge\sqrt B.
\tag{11}
\]

For each `n`, let `H_n` and `d_n` be the exact `FD-193` witness, so

\[
H_n=\Theta_B(n^2),
\qquad
n+1\le d_n\le Bn,
\qquad
d_n\le K_{H_n},
\qquad
\left\lfloor\frac{H_n}{d_n}\right\rfloor=n.
\tag{12}
\]

If for some exponents `sigma in [0,1]` and `gamma>=0`

\[
\boxed{
\mathcal E_{H,\sigma}(K_H)
=O_\varepsilon(H^{\gamma+\varepsilon})
}
\tag{13}
\]

holds on the geometric schedule for every `epsilon>0`, then (7)--(12) imply

\[
\boxed{
M(n)=O_\varepsilon
\left(n^{\gamma+\sigma-1+\varepsilon}\right).
}
\tag{14}
\]

Consequently the Littlewood/RH-facing Mertens exponent `1/2` is reached by this weighted one-row route exactly on or below the line

\[
\boxed{
\gamma+\sigma\le\frac32.
}
\tag{15}
\]

This packages the `FD-195` obstruction and a new alternative in one diagram. At the classical Franel weight `sigma=1`, one needs `gamma<=1/2`, reproducing the `FD-195` requirement that the scalar Franel energy be smaller by an extra half power. At the half-Sobolev weight `sigma=1/2`, the ordinary horizon-scale budget

\[
\boxed{
\mathcal E_{H,1/2}(K_H)
=O_\varepsilon(H^{1+\varepsilon})
}
\tag{16}
\]

would already imply

\[
M(n)=O_\varepsilon(n^{1/2+\varepsilon}).
\tag{17}
\]

The important negative statement is that (16) is **not** hidden inside the classical Franel estimate by a change of norm. On a square-root band and for `0<=sigma<=1`,

\[
\mathcal E_{H,\sigma}(K_H)
\le
K_H^{2(1-\sigma)}
\mathcal E_{H,1}(K_H).
\tag{18}
\]

The classical RH-scale Franel bound gives only

\[
\mathcal E_{H,1}(K_H)
\le
\mathcal E_{H,1}(\infty)
=O_\varepsilon(H^{1+\varepsilon}),
\tag{19}
\]

and hence only

\[
\boxed{
\mathcal E_{H,\sigma}(K_H)
=O_\varepsilon(H^{2-\sigma+\varepsilon}).
}
\tag{20}
\]

The inherited exponent is `gamma=2-sigma`, so

\[
\gamma+\sigma=2
\tag{21}
\]

for **every** weight in the interpolation family. Substituting into (14) again gives only

\[
M(n)=O_\varepsilon(n^{1+\varepsilon}).
\tag{22}
\]

The critical budget in (15) is

\[
\gamma=\frac32-\sigma,
\tag{23}
\]

which is always exactly one half power of `H` smaller than the generic consequence (20). Thus the missing half power isolated by `FD-195` is invariant under this whole fractional-Sobolev reweighting. A new proof must create actual spectral suppression, source-specific coupling, or cross-horizon cancellation; merely measuring the same signed modes in a stronger norm cannot manufacture the gain.

## 1. Exact weighted row norm

From the divisor transform (1), ordinary Möbius inversion gives (6). Apply Cauchy--Schwarz with weights `e^{-2sigma}`:

\[
\begin{aligned}
\left|M\!\left(\left\lfloor\frac Hd\right\rfloor\right)\right|^2
&\le
\left(
\frac1{d^2}
\sum_{e\mid d}
\mu(d/e)^2 e^{2\sigma}
\right)
\left(
\sum_{e\mid d}
\frac{|\mathcal B_H(e)|^2}{e^{2\sigma}}
\right)\\
&\le
\left(
\frac1{d^2}
\sum_{e\mid d}
\mu(d/e)^2 e^{2\sigma}
\right)
\mathcal E_{H,\sigma}(K),
\end{aligned}
\tag{24}
\]

because every divisor of `d<=K` also lies in the retained initial band. Put `r=d/e`. Then

\[
\frac1{d^2}
\sum_{e\mid d}
\mu(d/e)^2 e^{2\sigma}
=
d^{2\sigma-2}
\sum_{r\mid d}
\frac{\mu(r)^2}{r^{2\sigma}}
=
d^{2\sigma-2}
\prod_{p\mid d}(1+p^{-2\sigma}),
\tag{25}
\]

which is (8).

The exact-dual-norm claim is also immediate. In the Hilbert space of arbitrary complex band data `z=(z_k)_(k<=K)` with

\[
\|z\|_{\sigma,K}^2
=\sum_{k\le K}|z_k|^2/k^{2\sigma},
\tag{26}
\]

the coordinate functional

\[
L_d(z)
=
\frac1d\sum_{e\mid d}\mu(d/e)z_e
\tag{27}
\]

has squared Riesz norm exactly (25). Equality in weighted Cauchy is attained by the usual Riesz vector. This sharpness is deliberately a statement about unrestricted band data. Physical Farey spectra satisfy additional arithmetic and cross-horizon relations, and those relations are precisely where a stronger theorem would have to enter.

## 2. The Euler factor is subpower

For every `eta>0` and every fixed `sigma>=0`, all sufficiently large primes satisfy

\[
1+p^{-2\sigma}\le p^\eta.
\tag{28}
\]

The finitely many smaller primes contribute a constant depending only on `sigma,eta`. Therefore

\[
\prod_{p\mid d}(1+p^{-2\sigma})
\ll_{\sigma,\eta} d^\eta,
\tag{29}
\]

which proves (9)--(10). This argument includes the endpoint `sigma=0`, where the product is simply `2^{\omega(d)}`.

Apply (7) at the `FD-193` witness `(H_n,d_n)`. Since `d_n=Theta_B(n)` and `H_n=Theta_B(n^2)`, equations (10) and (13) give

\[
|M(n)|^2
\ll_{B,\varepsilon}
H_n^{\sigma-1+o(1)}
H_n^{\gamma+\varepsilon}
=
n^{2(\gamma+\sigma-1)+o(1)+O(\varepsilon)}.
\tag{30}
\]

Taking square roots and absorbing the subpower factor into `epsilon` proves (14). The condition (15) is then exactly the point where the generic recovered exponent reaches `1/2`.

## 3. Classical Franel energy stays a half power above the critical line

At `sigma=1`, `FD-002` gives the complete spectral identity

\[
\mathcal E_{H,1}(\infty)
=
2\pi^2
\left(L_H\mathfrak F_H+\frac1{12}\right),
\tag{31}
\]

with `L_H=Theta(H^2)`. The classical Franel--Landau RH scale

\[
\mathfrak F_H=O_\varepsilon(H^{-1+\varepsilon})
\tag{32}
\]

therefore corresponds to

\[
\mathcal E_{H,1}(\infty)
=O_\varepsilon(H^{1+\varepsilon}).
\tag{33}
\]

Using only the finite-band norm comparison (18), this transfers to (20). The gap between the inherited exponent `2-sigma` and the critical exponent `3/2-sigma` is

\[
(2-\sigma)-(3/2-\sigma)=1/2
\tag{34}
\]

independently of `sigma`.

This is the main hostile check against a fake improvement by renorming. At `sigma=1/2`, for example, the classical `L^2` estimate supplies only

\[
\mathcal E_{H,1/2}(K_H)
=O_\varepsilon(H^{3/2+\varepsilon}),
\tag{35}
\]

whereas the RH-facing recovery route needs (16), namely `O(H^{1+epsilon})`. Exactly the same missing factor `H^{1/2}` remains.

At the other endpoint, keeping `sigma=1` but demanding `gamma=1/2` is exactly the stronger scalar-energy requirement already isolated in `FD-195`. Thus (15) does not evade that obstruction; it shows the continuum of ways in which the same half-power deficit can be supplied.

## 4. Representation audit and prior-art boundary

The observation geometry is unchanged. `mathcal B_H(k)` is the same signed Farey Fourier/divisor-transform coordinate already derived in `FD-002/FD-117`, and `K_H` is the same complete geometric square-root band classified by `FD-193`. No source coefficient, prime-extension observable, or off-band Fourier mode is added. The only new object is the diagonal weight assigned to already retained modes.

That distinction matters because the norm is genuinely stronger. Equation (18) quantifies the largest power lost in passing from classical Franel `L^2` to the weighted band norm, and equations (20)--(34) show that the change alone preserves the bad Mertens exponent. The useful half-Sobolev estimate (16) is therefore a new analytic statement, not a rewriting of the classical Franel criterion.

Harmonic and norm-based formulations of Farey discrepancy are classical territory; the line already anchors Codecà--Perelli for `l^p` harmonic analysis. A recent neighboring result is Toni Karvonen and Anatoly Zhigljavsky, *Maximum mean discrepancies of Farey sequences*, Acta Mathematica Hungarica **177** (2025), 351--362, DOI `10.1007/s10474-025-01577-5`, which gives RH-equivalent MMD rates for broad RKHS classes and includes Matérn kernels of order at least `1/2`. Their Matérn RKHSs are identified with Sobolev spaces `W^{nu+1/2,2}`, so the paper is an important warning against claiming that Sobolev/kernel discrepancy viewpoints themselves are new. The present statement is narrower and different: it derives the exact dual exponent of the `FD-117` divisor inversion on a moving finite square-root Fourier band and locates the invariant half-power loss relative to the classical Franel norm. No theorem from that paper is used in the derivation above, so it is not a new load-bearing source for `SOURCES.md` under the line's source-expansion rule.

The sharpness qualifier is also representation-specific. Equation (8) is exact for unrestricted weighted band data, but a physical Farey spectrum is not an arbitrary vector in that Hilbert space. Source arithmetic, relations among Fourier modes, or coherent information across horizons may lower the effective dual cost. This finding classifies the generic diagonal-weight route; it does not rule out precisely those stronger structures.

## 5. Research consequence

`FD-195` left the destination norm as one plausible place where the raw divisor inverse might retain its contraction. The weighted phase diagram now makes that target precise. On the minimal geometrically complete square-root band, the cleanest RH-facing target is

\[
\boxed{
\sum_{k\le c\sqrt H}
k\,|\widehat R_H(k)|^2
=O_\varepsilon(H^{1+\varepsilon}),
\qquad c\ge\sqrt B,
}
\tag{36}
\]

along `H=B^m`. Up to the fixed factor `4pi^2`, this is exactly (16), and it would transfer through the stable `FD-193/194` recovery geometry to the Littlewood Mertens scale.

The finding does **not** provide (36). More importantly, classical Franel control cannot provide it through generic finite-band norm comparison: it misses by `H^{1/2}`. A productive next step therefore has to explain why the physical Farey spectrum suppresses this half-Sobolev band energy beyond what total `L^2` mass permits, or replace diagonal Sobolev weighting by a relation-sensitive/cross-horizon statistic. This keeps the open problem on the physical Farey side rather than hiding the missing power inside notation.

## Formalization disposition

No formalization issue is opened. The finite identity (25) is a short Möbius-inversion plus weighted Cauchy--Schwarz calculation, while the substantive content of the finding is the asymptotic interaction with the geometric witness and the Franel scaling. Formalizing the isolated row identity would add little structural coverage beyond the already explicit divisor-inversion machinery.