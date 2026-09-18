# FD-201 — Fixed-mode cross-horizon positive energy still overcoerces multiplicative Mertens shells

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** cross-horizon Fourier algebra / fixed-mode differencing / positive-energy route restriction
- **Depends on:** FD-117, FD-196, FD-197, FD-198, FD-199, FD-200
- **Classification:** `EXACT-DERIVED + CROSS-HORIZON-SOURCE-SENSITIVE + PRIME-SHELL-RMS + RANDOM-MULTIPLICATIVE-BASELINE + NEGATIVE/ROUTE-RESTRICTION`

## Claim

`FD-200` rules out matched horizon-mode dilation because it is universal divisor transport. Keeping the Fourier mode fixed while changing the horizon does escape that algebraic redundancy: it sees a genuine source increment. However, if that fixed-mode difference is immediately compressed into a positive diagonal half-Sobolev energy, the same shellwide overcoercion exposed by `FD-198`--`FD-199` returns.

Let `A(0)=0` be any cumulative source and

\[
\mathcal B_H(k)
:=
\sum_{d\mid k}d\,A\!\left(\left\lfloor\frac Hd\right\rfloor\right).
\tag{1}
\]

Fix an integer `r>=2` and define the fixed-mode cross-horizon difference

\[
D_{r,H}(k):=\mathcal B_{rH}(k)-\mathcal B_H(k).
\tag{2}
\]

For every prime `p`, the same-horizon prime-row identity at the two horizons gives

\[
\boxed{
D_{r,H}(p)-D_{r,H}(1)
=
p\left[
A\!\left(\left\lfloor\frac{rH}{p}\right\rfloor\right)
-
A\!\left(\left\lfloor\frac H p\right\rfloor\right)
\right].
}
\tag{3}
\]

Unlike the matched dilation of `FD-200`, (3) is not universal redundancy: the bracket changes with the source. For the physical source `A=M`, write

\[
\Delta_{r,H}(p)
:=
M\!\left(\left\lfloor\frac{rH}{p}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac H p\right\rfloor\right)
=
\sum_{\lfloor H/p\rfloor<n\le \lfloor rH/p\rfloor}\mu(n).
\tag{4}
\]

Thus fixed-mode cross-horizon subtraction exactly exposes a Möbius sum over a **fixed-ratio multiplicative interval**. The interval length is comparable to its left endpoint when `r` is fixed; this is not a "short interval" in the usual additive analytic-number-theory sense.

Now put

\[
K:=\lfloor\sqrt H\rfloor,
\qquad
\mathcal D_{r,H}(K)
:=
\sum_{k\le K}\frac{|D_{r,H}(k)|^2}{k}.
\tag{5}
\]

On the prime shell `K/2<p<=K`, define the centered shell energy

\[
\mathcal X_{r,H}
:=
\sum_{K/2<p\le K}
\frac{|D_{r,H}(p)-D_{r,H}(1)|^2}{p}.
\tag{6}
\]

Then

\[
\boxed{
\mathcal X_{r,H}
=
\sum_{K/2<p\le K}p\,|\Delta_{r,H}(p)|^2
\le
(1+o(1))\,\mathcal D_{r,H}(K).
}
\tag{7}
\]

Consequently,

\[
\boxed{
\sum_{K/2<p\le K}|\Delta_{r,H}(p)|^2
\le
(2+o(1))\frac{\mathcal D_{r,H}(K)}K.
}
\tag{8}
\]

Since `pi(K)-pi(K/2)~K/(2 log K)`, this yields

\[
\boxed{
\operatorname{RMS}_{K/2<p\le K}\Delta_{r,H}(p)
\ll
\left(\frac{\mathcal D_{r,H}(K)\log K}{K^2}\right)^{1/2}.
}
\tag{9}
\]

In particular, a positive cross-horizon budget at the same critical size suggested by the half-Sobolev recovery line,

\[
\mathcal D_{r,H}(K)=O_\varepsilon(H^{1+\varepsilon}),
\tag{10}
\]

would force

\[
\operatorname{RMS}_{K/2<p\le K}\Delta_{r,H}(p)
=K^{o(1)}.
\tag{11}
\]

So fixed-mode differencing does create new arithmetic information, but **squaring all of it into a positive half-Sobolev norm still demands simultaneous subpower cancellation on a growing reciprocal-prime shell**.

The squarefree Rademacher random multiplicative control confirms that the missing half power survives the horizon difference. If `f` is the standard squarefree random multiplicative source, then

\[
\boxed{
\mathbb E\,\mathcal X_{r,H}
\sim
\frac{3(r-1)}{\pi^2}\frac{HK}{\log K}
=
H^{3/2+o(1)}.
}
\tag{12}
\]

Thus even the **prime shell alone** retains the `FD-197` random-multiplicative scale. The route restriction is therefore sharper than `FD-200`: matched horizon-mode differences are algebraically sterile, whereas fixed-mode horizon differences are source-sensitive but a uniformly positive diagonal norm still destroys the sign/correlation information one hoped to exploit.

## 1. Exact fixed-mode prime-shell identity

For a prime `p`, (1) has only the divisors `1,p`, so

\[
\mathcal B_H(p)
=
A(H)+pA\!\left(\left\lfloor\frac Hp\right\rfloor\right),
\qquad
\mathcal B_H(1)=A(H).
\tag{13}
\]

Subtracting the centered prime row at horizon `H` from the same centered row at horizon `rH` gives

\[
\begin{aligned}
D_{r,H}(p)-D_{r,H}(1)
&=
[\mathcal B_{rH}(p)-\mathcal B_{rH}(1)]
-[\mathcal B_H(p)-\mathcal B_H(1)]\\
&=
p\left[
A\!\left(\left\lfloor\frac{rH}{p}\right\rfloor\right)
-
A\!\left(\left\lfloor\frac Hp\right\rfloor\right)
\right],
\end{aligned}
\tag{14}
\]

which proves (3). For `A=M`, the bracket telescopes to the Möbius sum (4) with no approximation and no inversion of the observation map.

The reciprocal-prime samples are genuinely distinct. If `K/2<p<q<=K` are primes, then `q-p>=2` and

\[
\frac Hp-\frac Hq
=
\frac{H(q-p)}{pq}
\ge
\frac{2H}{K^2}
\ge2.
\tag{15}
\]

Hence the lower endpoints `floor(H/p)` are distinct. The upper endpoints at horizon `rH` are separated even more strongly. The intervals can overlap, but they are not repeated copies of one sample as in the matched ridge of `FD-200`.

This is the precise sense in which fixed-mode comparison passes the first post-`FD-200` test: it changes the quotient coordinate rather than transporting the same one through the divisor lattice.

## 2. Positive half-Sobolev compression reintroduces shellwide overcoercion

Equation (3) immediately gives the equality in (7). To compare the centered shell with the raw positive energy, introduce measurement coordinates

\[
u_0:=D_{r,H}(1),
\qquad
u_p:=\frac{D_{r,H}(p)}{\sqrt p},
\qquad
v_p:=\frac1{\sqrt p}.
\tag{16}
\]

The centered vector has entries

\[
\nu_p-v_p\nu_0.
\tag{17}
\]

Exactly as in `FD-199`, the operator `T(nu_0,nu)=nu-v nu_0` satisfies

\[
TT^*=I+vv^*,
\qquad
\|T\|^2
=
1+\|v\|_2^2
=
1+\sum_{K/2<p\le K}\frac1p.
\tag{18}
\]

The prime number theorem gives

\[
\sum_{K/2<p\le K}\frac1p
\sim
\frac{\log 2}{\log K}
=o(1).
\tag{19}
\]

Since the coordinates in (16) are a subset of the coordinates entering (5), (18)--(19) prove the inequality in (7). Because every shell prime exceeds `K/2`, (8) follows. Dividing by

\[
N_K:=\pi(K)-\pi(K/2)
\sim
\frac{K}{2\log K}
\tag{20}
\]

then gives (9).

If (10) holds, `H=K^2(1+o(1))` converts (9) into

\[
\operatorname{RMS}\Delta_{r,H}(p)
\ll_\varepsilon
K^\varepsilon\sqrt{\log K},
\tag{21}
\]

which is the subpower statement (11) in the usual `epsilon` sense.

This should not be misread as evidence that (10) is false. It is a route audit. The same phenomenon found in `FD-198` survives after replacing endpoint values `M(floor(H/p))` by genuine cross-horizon increments. Therefore a proof strategy based on making the **entire positive diagonal cross-horizon energy** critically small would again be proving much more simultaneous cancellation than the one-coordinate RH scale asks for.

## 3. Random multiplicative control: the half-power deficit survives differencing

Let `f` be the squarefree Rademacher random multiplicative function,

\[
f(n)=\mu(n)^2\prod_{p\mid n}X_p,
\tag{22}
\]

where the `X_p` are independent Rademacher signs. As in `FD-197`,

\[
\mathbb E[f(m)f(n)]
=
\mu(n)^2\mathbf 1_{m=n}.
\tag{23}
\]

For

\[
I_p
:=
\left(
\left\lfloor\frac Hp\right\rfloor,
\left\lfloor\frac{rH}{p}\right\rfloor
\right],
\tag{24}
\]

orthogonality gives exactly

\[
\mathbb E
\left|\sum_{n\in I_p}f(n)\right|^2
=
\sum_{n\in I_p}\mu(n)^2.
\tag{25}
\]

The standard squarefree count

\[
\sum_{n\le x}\mu(n)^2
=
\frac6{\pi^2}x+O(\sqrt x)
\tag{26}
\]

is uniform enough here because `H/p=Theta(K)` on the shell. Therefore

\[
\mathbb E
\left|\sum_{n\in I_p}f(n)\right|^2
=
\frac6{\pi^2}(r-1)\frac Hp
+O_r(\sqrt K).
\tag{27}
\]

Multiplying by `p=Theta(K)` gives

\[
p\,\mathbb E
\left|\sum_{n\in I_p}f(n)\right|^2
=
\frac6{\pi^2}(r-1)H
+O_r(K^{3/2}).
\tag{28}
\]

Since `H=K^2(1+o(1))`, the error is lower order uniformly over the shell. Summing (28) over the primes and using (20) yields

\[
\mathbb E\,\mathcal X_{r,H}
\sim
\frac6{\pi^2}(r-1)H\frac{K}{2\log K}
=
\frac{3(r-1)}{\pi^2}\frac{HK}{\log K},
\tag{29}
\]

which proves (12).

Thus cross-horizon differencing does not by itself manufacture the missing `H^(1/2)` suppression. The source has exact squarefree multiplicativity and exact second-moment cancellation, yet the prime shell already costs `H^(3/2+o(1))`. Any deterministic Möbius gain down to the positive budget (10) would again need structure that the random multiplicative model lacks.

## 4. What this rules out, and what remains live

`FD-200` and `FD-201` separate two superficially similar cross-horizon constructions.

- Matched scaling `(H,k)->(pH,pk)` is universal divisor transport; its residual contains no source-specific arithmetic information.
- Fixed-mode scaling `(H,k)->(rH,k)` is source-sensitive and, at prime modes, exactly measures multiplicative-interval Möbius increments. But if those increments are squared independently and summed with positive half-Sobolev weights, the resulting critical budget overcontrols an entire reciprocal-prime shell and retains the random `H^(3/2+o(1))` baseline.

The negative conclusion is deliberately limited to the second step. Equation (3) shows that fixed-mode cross-horizon data are genuinely informative; `FD-201` does **not** say that cross-horizon comparison is useless. It says that the promising information is lost if one immediately removes all sign/cross-mode/cross-horizon correlations by diagonal positive squaring.

The remaining high-value route is therefore narrower: keep the source-sensitive fixed-mode increments, but combine them through a signed bilinear/covariance statistic, a targeted projection, an unmatched quotient-coordinate relation, or an order-sensitive/nonlinear Farey observable **before** norm compression. Any such proposal should be tested against both the universal cocycle of `FD-200` and the prime-shell random baseline (29).

## 5. Representation, prior-art and formalization audits

The representation audit is clean. Both `B_(rH)(p)` and `B_H(p)` are native signed Farey/divisor coordinates at physical horizons, and (14) is obtained by subtracting exact observation identities. The source increment in (3) is not inserted by applying an inverse source map. In particular, the contrast with `FD-200` is representation-native: matched dilation preserves the quotient `H/k`, whereas fixed-mode horizon dilation changes it.

The positive-energy restriction is equally explicit. The theorem does not claim that the raw signed family `(D_(r,H)(k))` is insufficient; only that the diagonal quadratic compression (5) at the critical positive scale has the shellwide consequence (11). The random multiplicative model is introduced at the source before applying the same observation map, so (29) is not an artifact of independent Fourier noise.

A targeted prior-art search found the established literature on cancellation of Möbius and general multiplicative functions in additive short intervals, notably Matomäki--Radziwiłł and later all-short-interval results, but no direct formulation of the reciprocal-prime fixed-ratio shell (3)--(12) in the Farey/Mertens transform. Those additive short-interval theorems are adjacent context rather than inputs here: the intervals in (4) have length comparable to their location for fixed `r`. No external theorem beyond standard prime and squarefree counting is load-bearing, so `SOURCES.md` is unchanged.

No formalization issue is opened. The finite algebraic core is the prime-row subtraction plus the rank-one centering estimate already isolated in `FD-199`; the useful content is the asymptotic route classification and the random-multiplicative benchmark rather than a new difficult standalone lemma.
