# FD-275 — Clustered zero packets have only linear band amplification before background conditioning

- **Date:** 2026-09-22
- **Status:** proved exact packet-integral band bound; threshold consequence conditional on simple critical-line clusters
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** zeta-zero clusters / Mellin finite differences / divisor replication / one-sided repair / background conditioning
- **Depends on:** FD-261, FD-271, FD-274
- **Classification:** `EXACT-DERIVED + MELLIN-INTEGRAL-KERNEL + CLUSTER-BAND-L1 + BACKGROUND-CONDITIONING-TARIFF`

## Claim

FD-274 shows that the apparent inverse-gap singularities of a finite simple-zero cluster cancel exactly after the cluster residues are summed. Its remaining escape route is that the desingularized background

\[
H_{\mathcal C}(s)
=
\frac{\zeta(s)}{\prod_{\rho\in\mathcal C}(s-\rho)}
\]

or its derivatives could still be badly conditioned. The packet kernel itself can now be separated quantitatively from that background.

For the normalized finite-zero repair packet of FD-271/FD-274, write

\[
K_s(d)
=
\sum_{q\mid d}\bigl(q^s-(q-1)^s\bigr),
\qquad
A_{N,d}(s)
=
N^{s-1/2}\frac{K_s(d)}{s}.
\tag{1}
\]

For every integer `r>=0` and every `Re s>0`, there is the exact integral identity

\[
\boxed{
A_{N,d}^{(r)}(s)
=
N^{s-1/2}
\sum_{q\mid d}
\int_{q-1}^{q}
 t^{s-1}\bigl(\log(Nt)\bigr)^r\,dt .
}
\tag{2}
\]

The `q=1` integral is an improper integral at zero and converges for `Re s>0`. In particular, on the critical line the modulus of the integrand in (2) is independent of the zero ordinate:

\[
\left|
N^{s-1/2}t^{s-1}
\right|
=t^{-1/2},
\qquad \Re s=\frac12.
\tag{3}
\]

Let `x>=2`, `N>=1`, and put

\[
L_{N,x}=1+\log(2Nx).
\]

Then for each fixed `r`, uniformly over **any** vertical segment `I` of the critical line,

\[
\boxed{
\sum_{x<d\le2x}
\sup_{s\in I}|A_{N,d}^{(r)}(s)|
\ll_r
xL_{N,x}^{\,r}.
}
\tag{4}
\]

Thus differentiation of the analytic packet amplitude has only linear divisor-band cost, up to powers of a logarithm. There is no hidden factor depending polynomially on the zero height or on the inverse internal gap.

Now let

\[
\mathcal C=\{\rho_1,\ldots,\rho_m\}
\]

be a consecutive cluster of distinct simple critical-line zeros whose joining segment `I_C` contains no zero after the cluster itself is factored out, and write

\[
\zeta(s)=P_{\mathcal C}(s)H_{\mathcal C}(s),
\qquad
P_{\mathcal C}(s)=\prod_{j=1}^m(s-\rho_j).
\]

Define the background derivative ledger

\[
B_j(\mathcal C)
=
\sup_{s\in I_{\mathcal C}}
\left|
\left(\frac{d}{ds}\right)^j
H_{\mathcal C}(s)^{-1}
\right|.
\tag{5}
\]

The contribution of this cluster to one normalized complex repair coordinate is

\[
Q_{\mathcal C}(N,d)
=
\sum_{\rho\in\mathcal C}
N^{i\operatorname{Im}\rho}
\frac{K_\rho(d)}{\rho\zeta'(\rho)}.
\tag{6}
\]

By the exact FD-274 divided-difference identity, Hermite--Genocchi, Leibniz, and (4),

\[
\boxed{
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|
\ll_m
x
\sum_{r=0}^{m-1}
L_{N,x}^{\,r}
B_{m-1-r}(\mathcal C).
}
\tag{7}
\]

The real packet adds only the harmless factor coming from `2 Re`. Therefore a bounded-size close cluster has **only linear depth amplification before the desingularized background is charged**.

For a pair this is especially transparent:

\[
\boxed{
\sum_{x<d\le2x}|Q_{\{\rho_-,\rho_+\}}(N,d)|
\ll
x\bigl(B_1+L_{N,x}B_0\bigr).
}
\tag{8}
\]

Consequently, in the polynomial-depth regime relevant to FD-261, where `x=N^{lambda+o(1)}` for fixed `lambda>0`, one has `L_{N,x}=x^{o(1)}`. If a fixed-size cluster by itself contributes at the positive-capacity threshold

\[
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|
\ge
x^{2-\beta-o(1)},
\qquad
\beta=\log_2\frac32,
\tag{9}
\]

then (7) forces

\[
\boxed{
\max_{0\le j\le m-1}B_j(\mathcal C)
\ge
x^{1-\beta-o(1)}
=
x^{0.4150374992\ldots-o(1)}.
}
\tag{10}
\]

So after the internal close-gap singularity is removed, a bounded cluster cannot recover the missing power through packet differentiation. It must carry a genuinely polynomial **external/background conditioning defect**.

## Evidence

For `Re s>0`, the fundamental theorem of calculus gives

\[
\frac{q^s-(q-1)^s}{s}
=
\int_{q-1}^{q}t^{s-1}\,dt.
\tag{11}
\]

Summing (11) over `q|d` and multiplying by `N^{s-1/2}` gives (2) for `r=0`. Differentiation under each finite integral gives the general case because

\[
\frac{d^r}{ds^r}
\left(N^{s-1/2}t^{s-1}\right)
=
N^{s-1/2}t^{s-1}
\bigl(\log(Nt)\bigr)^r.
\]

On `Re s=1/2`, define

\[
J_{q,r}
=
\int_{q-1}^{q}
 t^{-1/2}|\log(Nt)|^r\,dt.
\]

For `q>=2`,

\[
J_{q,r}
\ll_r
q^{-1/2}L_{N,x}^{\,r}
\qquad (q\le2x),
\tag{12}
\]

while the endpoint interval satisfies

\[
J_{1,r}
=
\int_0^1t^{-1/2}|\log(Nt)|^r\,dt
\ll_r
(1+\log N)^r.
\tag{13}
\]

After summing over the depth band and interchanging the divisor and depth sums, the number of `d` in `(x,2x]` divisible by `q` is at most `x/q+1`. Hence

\[
\begin{aligned}
\sum_{x<d\le2x}\sup_{\Re s=1/2}|A_{N,d}^{(r)}(s)|
&\le
\sum_{q\le2x}
\left(\frac{x}{q}+1\right)J_{q,r}\\
&\ll_r
xL_{N,x}^{\,r}
\sum_{q\ge2}q^{-3/2}
+
L_{N,x}^{\,r}
\sum_{q\le2x}q^{-1/2}
+
xJ_{1,r}\\
&\ll_r xL_{N,x}^{\,r},
\end{aligned}
\tag{14}
\]

which proves (4). The second sum is only `O(x^(1/2))` and is absorbed by the first-scale bound.

FD-274 gives exactly

\[
Q_{\mathcal C}(N,d)
=
[\rho_1,\ldots,\rho_m]
\left(\frac{A_{N,d}}{H_{\mathcal C}}\right).
\tag{15}
\]

Parametrizing the critical-line segment by its ordinate changes divided differences and derivatives only by unit powers of `i`. Hermite--Genocchi therefore yields

\[
|Q_{\mathcal C}(N,d)|
\le
\frac1{(m-1)!}
\sup_{s\in I_{\mathcal C}}
\left|
\left(\frac d{ds}\right)^{m-1}
\left(A_{N,d}(s)H_{\mathcal C}(s)^{-1}\right)
\right|.
\tag{16}
\]

Leibniz expands the derivative in (16) into

\[
\sum_{r=0}^{m-1}
\binom{m-1}{r}
A_{N,d}^{(r)}(s)
\left(H_{\mathcal C}^{-1}\right)^{(m-1-r)}(s).
\]

Summing in `d`, inserting (4) and absorbing the fixed combinatorial factors proves (7). Equation (10) then follows because for fixed `m` and polynomial divisor depth every power of `L_{N,x}` is `x^{o(1)}`.

## Stress tests

The first stress test is the `q=1` endpoint. Formula (2) integrates down to zero, where powers of `log t` diverge. The weight `t^(-1/2)` is nevertheless integrable against every fixed logarithmic power, giving (13). Since `q=1` divides every `d`, this endpoint contributes `O_r(x(1+log N)^r)` to the band and is already included in the linear estimate; there is no missing singular cell.

The second stress test is frequency. Taking `s=1/2+iU` with arbitrarily large `U` changes only the oscillatory phase `t^(iU)` in (2). The absolute majorant in (3)--(4) is independent of `U`. This is stronger than merely capping frequency at the depth as in FD-268: after the `1/s` already present in the Mertens residue amplitude is combined with the consecutive difference, derivatives of the resulting analytic amplitude do not pay any polynomial frequency tariff.

The third stress test is the exact two-zero toy model

\[
Z_{a,b}(s)=(s-a)(s-b),
\]

for which `H_C=1`. The grouped residue is exactly the first divided difference of `A`, so (8) reduces to

\[
\sum_{x<d\le2x}|Q_{\{a,b\}}(N,d)|
\ll xL_{N,x},
\]

uniformly as `a-b` tends to zero. Thus even an arbitrarily tight pair does not produce a power of the inverse gap once the residues are combined.

A direct finite numerical audit of (11) was also performed for complex `s=1/2+13.7i`, `N=17` and `d=1,2,6,30`; the direct formula and the interval-integral formula agreed to floating-point precision. This is only a sanity check: (11) is an exact analytic identity.

## Prior-art check

The fundamental-theorem-of-calculus representation (11), Leibniz differentiation and Hermite--Genocchi/divided-difference bounds are classical facts and are not claimed as new. A targeted literature search for clustered zeta-zero residues, divided differences, Mellin finite differences, and explicit Mertens formulas found the classical divided-difference literature and the standard explicit-formula/reciprocal-derivative setting, but no source applying this exact interval representation to the FD-267--FD-274 consecutive-difference plus divisor-replication packet, nor a bandwise estimate equivalent to (7).

The substantive content here is therefore the repository-specific combination: the exact packet amplitude admits the interval representation (2); divisor multiplicity converts it to the linear band ledger (4); and FD-274's cluster compression then prices every bounded close cluster by the derivatives of the **external** factor `H_C^(-1)` as in (7). No external theorem is load-bearing, so `SOURCES.md` requires no new dependency.

## Implications

FD-273 forces any nonexceptional threshold-sized finite-packet coherence, under its RH hypotheses, toward close-gap zeros. FD-274 then removes the raw internal inverse-gap singularity. FD-275 goes one step further: **for every fixed-size cluster, the packet-side analytic variation itself has only linear depth cost.** Reaching the FD-261 threshold requires a polynomial defect in the desingularized background, not merely a small internal spacing or a large zero ordinate.

At cluster nodes,

\[
H_{\mathcal C}(\rho_j)
=
\frac{\zeta'(\rho_j)}{P_{\mathcal C}'(\rho_j)},
\]

so `H_C` is precisely what remains of the zeta derivative after the mutual cluster-gap factors have been divided out. Equation (10) therefore provides a quantitative diagnostic for the surviving close-gap route: a bounded cluster that matters at threshold must exhibit at least `x^(1-beta-o(1))` growth in some derivative of this external reciprocal background.

This also changes the useful next observable. Raw negative moments of `1/zeta'(rho)` mix internal gap geometry with external conditioning. A cluster-aware argument should instead estimate the distribution, mean square, or aggregate tails of the quantities `B_j(C)` or of the grouped divided differences themselves. If those ledgers are subpolynomial for bounded clusters on the source-selected horizons, bounded close clusters cannot supply the required positive-capacity escape.

## Limitations

The result does not bound `B_j(C)` for the actual Riemann zeta function. External zeros just outside the chosen cluster, rapid background variation, or another source of poor conditioning can make these quantities large. Equation (10) identifies the required resource; it does not prove that the resource is absent.

The clean exponent consequence is for fixed cluster size and for polynomial divisor depth, or more generally whenever `L_{N,x}=x^(o(1))`. If the cluster size grows, the derivative order grows as well and the fixed-`m` constants, logarithmic powers, and background derivatives must be tracked jointly. A large collection of individually moderate clusters can also accumulate; (7) is a single-cluster tariff, not yet an aggregate theorem for the complete close-gap packet.

As in FD-274, the cluster argument assumes distinct simple zeros. Multiple zeros require confluent residue/Hermite analysis. The explicit-formula remainder, zeros above the truncation height, and non-spectral switched-only repairs remain outside the claim.

Finally, the Hermite--Genocchi segment bound is used on a zero-free desingularized critical-line corridor. Under RH this is automatic for a consecutive critical-line cluster after all zeros on the segment are included. The exact packet-integral bound (2)--(4) itself is unconditional and does not use RH.

## Decisive audit

For any proposed bounded close-cluster mechanism, first rewrite its normalized coordinate through (2) and recombine the cluster by (15). If the proposed power amplification comes only from zero height, internal gap size, or differentiating the consecutive-difference kernel, (4) and (7) reduce it to linear band size up to logarithms.

A genuine threshold-sized bounded-cluster contribution must instead exhibit, directly and quantitatively, a background derivative satisfying the tariff (10), or violate one of the explicit hypotheses above. An aggregate close-gap construction must additionally show how many such cluster tariffs add coherently without reintroducing the phase-cancellation barrier of FD-270--FD-273.