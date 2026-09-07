# AF-174 — Gauge-quotient H-infinity has sharp fixed-degree Blaschke divisor fidelity

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `GAUGE-QUOTIENT`, `POSITIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-170 shows that complete finite Blaschke inner factors can become arbitrarily close in the ordinary `H^\infty` norm while their zero divisors stay a fixed distance apart when the degree grows. AF-173 then identifies the harmless unimodular output gauge and proves an exact quotient metric on the one-complex-parameter cyclic stratum. The missing fixed-degree statement is positive: after quotienting that output phase, the full inner factor does control its entire zero divisor, including multiplicity, with an explicit global Hölder modulus.

Let

\[
B(z)=\eta\prod_{i=1}^n \phi_{a_i}(z),
\qquad
C(z)=\xi\prod_{j=1}^n \phi_{b_j}(z),
\qquad |\eta|=|\xi|=1,
\tag{1}
\]

be finite Blaschke products of the same degree `n>=1`, with zeros repeated according to multiplicity, where

\[
\phi_a(z)=\frac{z-a}{1-\overline a z},
\qquad
\rho(z,w)=\left|\frac{z-w}{1-\overline w z}\right|
\tag{2}
\]

is the pseudohyperbolic metric. Define the output-gauge quotient distance

\[
\delta(B,C)
=
\inf_{|\lambda|=1}
\|B-\lambda C\|_{H^\infty}
\tag{3}
\]

and the multiplicity-aware pseudohyperbolic bottleneck distance between the two degree-`n` zero divisors

\[
d_{\mathrm{div}}(B,C)
=
\min_{\sigma\in S_n}
\max_i \rho(a_i,b_{\sigma(i)}).
\tag{4}
\]

Then

\[
\boxed{
 d_{\mathrm{div}}(B,C)
 \le
 \min\!\left\{1,(2n-1)\,\delta(B,C)^{1/n}\right\}.
}
\tag{5}
\]

Thus every fixed-degree stratum has a global recovery modulus from the complete inner factor modulo its irrelevant output phase. The exponent `1/n` is optimal on the full degree-`n` class: no estimate

\[
d_{\mathrm{div}}(B,C)
\le K_n\,\delta(B,C)^\alpha
\tag{6}
\]

with finite `K_n` can hold for all degree-`n` finite Blaschke products when `\alpha>1/n`.

The bound is deliberately multiplicity-aware. A weaker one-line consequence follows immediately by evaluating at the zeros:

\[
\boxed{
 d_H^\rho(\operatorname{supp} Z(B),\operatorname{supp} Z(C))
 \le \min\{1,\delta(B,C)^{1/n}\},
}
\tag{7}
\]

where `d_H^\rho` is Hausdorff distance between the distinct zero supports. Equation `(5)` adds the nontrivial matching/counting step that `(7)` alone does not provide.

The dependence on degree is essential, not a proof artifact. For the cyclic radial family from AF-170--AF-173, fixed source radii `0<r<s<1` give

\[
d_{\mathrm{div}}(B_{n,r},B_{n,s})=\rho(r,s)>0,
\tag{8}
\]

while

\[
\delta(B_{n,r},B_{n,s})
=2\rho(r^n,s^n)\longrightarrow0.
\tag{9}
\]

So the fixed-degree theorem cannot be upgraded to any degree-uniform inverse modulus in the unscaled divisor metric. AF-170's asymptotic obstruction and the present positive theorem are therefore two sides of the same conditioning law.

## Derivation

### Small quotient `H^\infty` error forces every source zero near some target zero

For every zero `a_i` of `B`,

\[
|C(a_i)|
=
\prod_{j=1}^n |\phi_{b_j}(a_i)|
=
\prod_{j=1}^n \rho(a_i,b_j).
\tag{10}
\]

Fix `\varepsilon>0` and choose `|\lambda|=1` with

\[
\|B-\lambda C\|_{H^\infty}
<\delta(B,C)+\varepsilon.
\tag{11}
\]

At `a_i`, equation `(11)` gives

\[
|C(a_i)|<\delta+\varepsilon.
\tag{12}
\]

If every `b_j` were farther than `(\delta+\varepsilon)^{1/n}` from `a_i` in pseudohyperbolic distance, the product in `(10)` would exceed `\delta+\varepsilon`, contradiction. Therefore

\[
\min_j\rho(a_i,b_j)
\le(\delta+\varepsilon)^{1/n}.
\tag{13}
\]

The same argument with `B` and `C` exchanged gives the reverse support inclusion. Letting `\varepsilon\downarrow0` proves `(7)`.

This support argument by itself does not control multiplicity: two multisets can have identical distinct support while assigning different multiplicities to the same support points. The full divisor estimate requires using the small function error on boundaries, not only at zeros.

### Rouche counting upgrades support proximity to a multiplicity-aware matching

Assume first `0<\delta<1` and choose any

\[
\delta^{1/n}<q<1.
\tag{14}
\]

Choose a phase `\lambda` so that

\[
\|B-\lambda C\|_{H^\infty}<q^n.
\tag{15}
\]

Around each zero `a_i`, repeated according to multiplicity but with coincident disks identified geometrically, take the pseudohyperbolic disk

\[
D_i=\{z\in\mathbb D:\rho(z,a_i)<q\},
\tag{16}
\]

and let

\[
U=\bigcup_i D_i.
\tag{17}
\]

On the boundary of every connected component of `U`, a point lies in none of the open disks. Hence for every `i`,

\[
\rho(z,a_i)\ge q,
\]

and therefore

\[
|B(z)|=\prod_{i=1}^n\rho(z,a_i)\ge q^n.
\tag{18}
\]

Together with `(15)`, Rouche's theorem implies that `B` and `\lambda C` have the same number of zeros, counted with multiplicity, inside each connected component of `U`. Since all `n` zeros of `B` lie in `U`, the component counts sum to `n`; consequently all `n` zeros of `C` also lie in `U`, with exactly the same zero count in each component.

Consider one component containing `m` zeros of `B`, counted with multiplicity. The distinct center disks in that component can be joined by an overlap chain. If two radius-`q` pseudohyperbolic disks overlap, the ordinary triangle inequality for `\rho` gives center distance at most `2q`. Hence any two source centers in the same component are at pseudohyperbolic distance at most

\[
2(m-1)q.
\tag{19}
\]

Every zero of `C` in the component lies in at least one radius-`q` source disk, so its distance to any chosen source center in that component is at most

\[
(2m-1)q.
\tag{20}
\]

Because the source and target zero counts agree component by component, choose any bijection within each component. Equation `(20)` gives a global matching with

\[
d_{\mathrm{div}}(B,C)
\le (2n-1)q.
\tag{21}
\]

Letting `q\downarrow\delta^{1/n}` proves `(5)` when `0<\delta<1`. If `\delta=0`, `B` and `C` agree up to a unimodular scalar and have the same zero divisor. If `\delta\ge1`, the trivial bound `d_{\mathrm{div}}\le1` completes `(5)`.

The constant `2n-1` is a coarse cluster-diameter bound and is not claimed sharp. The significant global statement is that the complete gauge-quotiented inner factor has a fixed-degree inverse modulus with exponent `1/n`, even without assuming simple or separated zeros.

### The exponent `1/n` is unavoidable

Take

\[
B_t(z)=z^n
\tag{22}
\]

and

\[
C_t(z)=\frac{z^n-t^n}{1-t^n z^n},
\qquad 0<t<1.
\tag{23}
\]

The zero divisor of `B_t` is the `n`-fold zero at the origin; the zeros of `C_t` are the simple regular polygon

\[
\{t e^{2\pi i j/n}:0\le j<n\}.
\tag{24}
\]

Therefore

\[
d_{\mathrm{div}}(B_t,C_t)=t.
\tag{25}
\]

AF-173's exact cyclic gauge formula, applied to coefficient parameters `0` and `t^n`, gives

\[
\delta(B_t,C_t)=2t^n.
\tag{26}
\]

If `(6)` held with `\alpha>1/n`, then

\[
t\le K_n 2^\alpha t^{n\alpha},
\]

which is impossible as `t\downarrow0`. Thus no globally valid power modulus can have exponent larger than `1/n` on the full degree-`n` class.

This sharpness mechanism is the same multiplicity-splitting geometry isolated for phase moments in AF-168, but here it acts directly on the complete inner function in the quotient `H^\infty` metric. Retaining all analytic modes does not remove the worst-case root-splitting exponent at fixed degree.

### Separated simple strata improve the counting geometry

The global constant in `(5)` pays for clusters. If the zeros of `B` are simple and pairwise separated by more than `2q`, where `q^n>\delta`, then the disks `(16)` are disjoint. Rouche's theorem gives exactly one zero of `C` in each disk, so the matching can be chosen with

\[
d_{\mathrm{div}}(B,C)\le q.
\tag{27}
\]

This does not claim that the optimal local dependence is only `1/n` on a fixed simple divisor. Classical simple-root perturbation gives a locally Lipschitz regime once the relevant derivative/separation constants are fixed. Equation `(27)` serves a narrower purpose: it shows directly how a source separation hypothesis removes the cluster-diameter penalty from the global quotient-metric argument.

## Prior art and novelty assessment

All complex-analysis ingredients are classical, and no novelty is claimed for the theorem as an isolated finite-Blaschke perturbation result.

- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, gives a modern treatment of finite Blaschke products, their zero sets, disk automorphisms, and hyperbolic/pseudohyperbolic geometry.
- John B. Garnett, ***Bounded Analytic Functions***, Graduate Texts in Mathematics 236, Springer (2007), DOI `10.1007/0-387-49763-3`, is a standard source for Blaschke products, interpolating sequences, and bounded analytic function theory.
- Artur Nicolau, **“Finite Products of Interpolating Blaschke Products,”** *Journal of the London Mathematical Society* 50(3), 520--531 (1994), DOI `10.1112/jlms/50.3.520`, is classical neighboring work on finite products of interpolating Blaschke products and the separation geometry of their zeros.
- Alexander Borichev, Artur Nicolau, Myriam Ounaïes, and Pascal J. Thomas, **“Sharp Invertibility in Quotient Algebras of H-infinity,”** *Journal of Functional Analysis* 290(11), 111417 (2026), DOI `10.1016/j.jfa.2026.111417`, develops modern sublevel-set/zero-set geometry for inner functions through sharp invertibility and related embedding properties. That theory is substantially broader than the elementary fixed-degree argument here and is useful prior-art context for the principle that quantitative lower bounds away from zeros encode recoverability.

A targeted search found mature zero-localization, interpolating-Blaschke, sublevel-set, and pseudohyperbolic geometry. The proof of `(5)` is only the elementary finite-degree product identity plus Rouche counting and cluster geometry, so no theorem-level novelty claim is warranted. The Arithmetic Fidelity contribution is the **metric placement relative to AF-170--AF-173**: the same complete inner representation that has no degree-uniform inverse in its ordinary asymptotic scaling does have a sharp-exponent fixed-degree recovery theorem after quotienting the harmless output phase.

## Boundary conditions and falsification checks

- Equation `(5)` assumes the two finite Blaschke products have the same known degree. If degree itself is compressed away, winding number or another retained datum must recover it before this theorem applies.
- The endpoint metric is the pseudohyperbolic bottleneck metric on zero divisors with multiplicity. Euclidean bottleneck metrics are comparable only on declared compact subdisks and require their own constants near the boundary.
- The gauge quotient removes only multiplication of the output by one unimodular scalar, which leaves the entire zero divisor unchanged. Quotienting a larger group can identify genuinely different divisors and requires a new fidelity audit.
- The `1/n` exponent is a worst-case global statement. At a fixed simple, separated divisor the inverse is locally better conditioned; AF-168 records the analogous multiplicity hierarchy in phase-moment coordinates.
- Conversely, the exponent cannot be made degree-independent on the full class. The sharpness family `(22)--(26)` and the fixed-radius growing-degree family `(8)--(9)` expose two complementary failures: multiplicity splitting at fixed degree and exponential radial attenuation as degree grows.
- The cluster constant `2n-1` is not asserted optimal. Improving constants without changing the admissible regime or asymptotic conclusion would not materially change the research frontier.
- Rouche counting uses exact `H^\infty` control of the complete analytic functions. A sampled boundary representation, finite moment vector, noisy phase profile, or another compressed readout requires a separate forward-error theorem before `(5)` can be invoked.
- No statement about Riemann-zeta zeros follows directly. An RH-facing use must identify why a finite-Blaschke or analogous inner representation is intrinsic, which zero-divisor endpoint is actually consumed downstream, and how its degree, separation, multiplicity, and data metric scale in the arithmetic limit.

## Consequences for the research line

AF-170 and AF-174 together separate **finite exact stability** from **asymptotic usefulness** without ambiguity. The complete inner factor is not intrinsically unstable: on each fixed-degree stratum it determines the full divisor with a quantitative global modulus. What fails in AF-170 is uniformity as complexity grows.

AF-173 adds the second necessary correction: the output phase is pure gauge and should be quotiented before measuring analytic fidelity. After that quotient, the audit becomes explicit:

\[
\text{complete inner factor modulo phase}
\xrightarrow[\text{fixed }n]{\text{Hölder }1/n}
\text{zero divisor},
\]

but the recovery exponent and constants depend on the complexity of the source stratum. A scalable arithmetic mechanism therefore has to declare **all four** of the quantities already highlighted by the local mind: endpoint quotient, data metric, complexity parameter, and asymptotic normalization. Exact completeness of the representation does not supply any of them for free.

For future RH-facing transfers, a useful question is no longer merely whether a compression retains the zero data. It is whether the admissible arithmetic family comes with a source-forced complexity/separation profile under which the inverse modulus remains nondegenerate in the exact metric consumed downstream. AF-174 provides a concrete positive benchmark against which such claims can be tested.