# WI-396 — zero density makes square-root-prime Fourier horizontal sensitivity vanish in density

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`. This finding does **not** improve the unconditional simple-critical zero proportion and does not prove RH. It combines the already-audited near-line zero-density input of WI-029 with the sharp weighted-Fourier contraction of WI-395. The result is an unconditional density-scale statement for the actual zeta zero multiset: after replacing every off-critical functional-equation mirror pair by two critical-line copies at the same ordinate, the two multisets become asymptotically indistinguishable to every scalar Fourier-Stieltjes test whose absolute source budget is measured by the square-root-prime weight `exp(|u|/2)`. Unlike WI-005/WI-006/WI-119, no lattice or special vertical arrangement of the zeros is assumed.

Let

\[
L_T:=\log(T/2\pi),
\qquad
N_T:=N(2T)-N(T),
\]

and let `E_T^+` be the multiset of zero occurrences

\[
\rho=\frac12+\delta_\rho+i\gamma_\rho,
\qquad
T<\gamma_\rho\le 2T,
\qquad
0<\delta_\rho<\frac12,
\]

on the right of the critical line, counted with multiplicity. Functional-equation symmetry pairs each such occurrence with `1/2-delta_rho+i gamma_rho` on the left. Let `q` be the sharp WI-395 contraction factor

\[
q(\delta)
=
\left(\frac{1-2\delta}{1+2\delta}\right)^{1/(2\delta)-1}
\left(\frac{4\delta}{1+2\delta}\right)^2,
\qquad 0<\delta<\frac12,
\]

with `q(0)=0`. Then

\[
\boxed{
Q_T:=\frac1{N_T}\sum_{\rho\in E_T^+}q(\delta_\rho)\longrightarrow0.
}
\tag{1}
\]

Consequently, if `mu` is any finite complex Borel measure with

\[
\|\mu\|_{1/2}
:=\int_{\mathbb R}e^{|u|/2}\,d|\mu|(u)<\infty
\]

and

\[
h(z):=\int_{\mathbb R}e^{iuz}\,d\mu(u),
\]

then

\[
\boxed{
\frac1{N_T}
\sum_{\rho\in E_T^+}
\left|
h(\gamma_\rho+i\delta_\rho)
+h(\gamma_\rho-i\delta_\rho)
-2h(\gamma_\rho)
\right|
\le Q_T\|\mu\|_{1/2}=o(1)\|\mu\|_{1/2}.
}
\tag{2}
\]

Equivalently,

\[
\boxed{
\sup_{\|\mu\|_{1/2}\le1}
\frac1{N_T}
\sum_{\rho\in E_T^+}
|\Delta_{\delta_\rho}h(\gamma_\rho)|
\longrightarrow0,
}
\tag{3}
\]

where `Delta_delta h(gamma)` denotes the mirror-pair discrepancy in (2). Thus the actual zeta zero multiset and its critical projection differ by `o(N_T)` in this normalized scalar test norm.

The research consequence is sharper than the fixed-depth contraction of WI-395. At density scale, a scalar architecture that pays the componentwise absolute square-root-prime Fourier budget has **vanishing horizontal sensitivity**, not merely a contraction by a fixed constant below one. Any source-side escape based on signed prime cancellation must therefore beat that absolute budget by a factor that diverges along the relevant test family, or else import information outside this scalar interface. This does not exclude a source-exact signed cancellation theorem, and it does not address an isolated fixed-depth RH counterexample.

## 1. The two exact inputs

WI-029 audits Jutila's unconditional near-line zero-density estimate. In the dyadic normalization above, if

\[
D_T(A)
:=\#\{\rho:T<\gamma\le2T,
\ |\beta-1/2|L_T>A\},
\]

counted with multiplicity, then for every fixed `epsilon>0` and every fixed `A>0`,

\[
\limsup_{T\to\infty}\frac{D_T(A)}{N_T}
\ll_\varepsilon e^{-(1-\varepsilon)A}.
\tag{4}
\]

The classical source is Matti Jutila, **Zeros of the zeta-function near the critical line**, in *Studies in Pure Mathematics to the Memory of Paul Turán* (1983), 385--394. WI-029 checks the conversion from Jutila's `N(sigma,T)` estimate to (4), including the dyadic normalization. No RH assumption enters.

WI-395 proves the sharp scalar inequality

\[
|h(\gamma+i\delta)+h(\gamma-i\delta)-2h(\gamma)|
\le q(\delta)\|\mu\|_{1/2},
\tag{5}
\]

for every `0<=delta<1/2`, together with `0<=q(delta)<1` and

\[
q(\delta)=\frac{16}{e^2}\delta^2+O(\delta^3)
\qquad(\delta\downarrow0).
\tag{6}
\]

The norm in (5) is exactly the absolute exponent-`1/2` Fourier cost corresponding to the square-root-prime crossover isolated in WI-393--WI-395. Equation (5), not an informal interpretation of it, is the only Fourier-analytic input below.

## 2. Zero density collapses the average contraction factor

Fix `A>0`. Split the right-half zero occurrences into the shallow set

\[
\delta_\rho L_T\le A
\]

and the deep set

\[
\delta_\rho L_T>A.
\]

For all sufficiently large `T`, `A/L_T<1/2`. Define

\[
r_T(A):=\sup_{0\le\delta\le A/L_T}q(\delta).
\tag{7}
\]

The expansion (6) implies

\[
r_T(A)=O_A(L_T^{-2})\longrightarrow0.
\tag{8}
\]

Every shallow occurrence contributes at most `r_T(A)`, and there are at most `N_T` of them. On the deep set use only `q<1`; its cardinality is at most `D_T(A)`. Therefore

\[
\boxed{
Q_T
\le r_T(A)+\frac{D_T(A)}{N_T}.
}
\tag{9}
\]

Taking `limsup` and using (4),

\[
\limsup_{T\to\infty}Q_T
\ll_\varepsilon e^{-(1-\varepsilon)A}.
\tag{10}
\]

Now let `A->infinity`. The right side tends to zero, while `Q_T>=0`. This proves (1).

The order of limits is important. No uniform-in-`A` strengthening of Jutila is being asserted. First `A` is held fixed while `T->infinity`; only after taking the `limsup` is `A` sent to infinity. Hence the argument uses exactly the zero-density statement already justified in WI-029. Notice also that monotonicity of the closed form for `q` is unnecessary: continuity and the quadratic expansion at zero suffice through the supremum in (7).

## 3. Uniform critical-projection theorem

Apply (5) separately to each right-half zero occurrence and sum absolute values. Multiplicity causes no issue because both Jutila's count and `E_T^+` are multisets. One obtains

\[
\sum_{\rho\in E_T^+}
|\Delta_{\delta_\rho}h(\gamma_\rho)|
\le
\|\mu\|_{1/2}
\sum_{\rho\in E_T^+}q(\delta_\rho).
\tag{11}
\]

Divide by `N_T` and use (1) to obtain (2). Since the right side depends on `h` only through `||mu||_(1/2)`, taking the supremum over the unit ball gives (3).

There is an exact zero-multiset formulation with no coordinate ambiguity. For a zero `rho=beta+i gamma` define the centered scalar evaluation

\[
\widetilde h_\mu(\rho)
:=h_\mu\!\left(\gamma+i(\beta-1/2)\right).
\tag{12}
\]

Let `Z_T` be the multiset of nontrivial zero occurrences with `T<gamma<=2T`, and let `Pi Z_T` be obtained by moving every occurrence horizontally to the critical line while preserving its ordinate and multiplicity. Critical-line occurrences are unchanged. Pairing right- and left-half zeros by the functional equation gives exactly

\[
\sum_{\rho\in Z_T}\widetilde h_\mu(\rho)
-
\sum_{\rho\in \Pi Z_T}\widetilde h_\mu(\rho)
=
\sum_{\rho\in E_T^+}
\Delta_{\delta_\rho}h_\mu(\gamma_\rho).
\tag{13}
\]

Therefore (11) implies

\[
\boxed{
\sup_{\|\mu\|_{1/2}\le1}
\frac1{N_T}
\left|
\sum_{\rho\in Z_T}\widetilde h_\mu(\rho)
-
\sum_{\rho\in \Pi Z_T}\widetilde h_\mu(\rho)
\right|
\longrightarrow0.
}
\tag{14}
\]

Equation (14) is merely the pairwise scalar estimate rewritten on the actual zeta multiset; it is not a new explicit-formula theorem. In particular, it does not claim that every finite measure `mu` is itself an admissible Weil test without the usual additional regularity assumptions.

## 4. What this does and does not close

Suppose a scalar test family `h_T` is required to produce a density-scale horizontal separation

\[
\frac1{N_T}
\sum_{\rho\in E_T^+}
|\Delta_{\delta_\rho}h_T(\gamma_\rho)|
\ge c>0.
\tag{15}
\]

Then (2) forces

\[
\boxed{
\|\mu_T\|_{1/2}\ge \frac{c}{Q_T}\longrightarrow\infty.
}
\tag{16}
\]

Thus no normalization in which the componentwise absolute square-root-prime Fourier cost remains `O(1)` can retain a positive density-scale horizontal signal. To turn such tests into a viable source-side argument, the **actual signed prime evaluation** would have to be smaller than the absolute norm by a ratio that compensates `Q_T->0`; equivalently, the gain over the absolute envelope must diverge. This is the precise surviving signed-cancellation gate left by WI-395.

The statement is deliberately not promoted beyond that interface. It does not say that actual prime-side cancellation of the required strength is impossible. It does not control matrix-valued or indefinite observables, vertical-spacing information, nonlinear statistics, or tests whose arithmetic cost is governed by a stronger source theorem than the absolute `exp(|u|/2)` envelope. Most importantly, it does not rule out a **sparse** RH counterexample: Jutila permits finitely many or zero-density zeros at fixed horizontal depth `delta>0`, and for such a packet `q(delta)` need not tend to zero. WI-205/WI-206 independently explain why one isolated normalized-depth residue is weak in the Gallagher source norm; the present result is different, because it controls the aggregate scalar horizontal discrepancy of the actual zero population without choosing a vertical localization architecture.

The finding also differs from WI-005/WI-006/WI-119. Those results construct or analyze critical-lattice screening and show exact blindness for specially arranged local configurations inside support-restricted test classes. Equation (14) assumes no lattice geometry and no correlation model. Its smallness comes from the arithmetic fact that, in density, actual off-line zeta zeros are forced into horizontal depth `o(1)` strongly enough for the sharp WI-395 contraction factor to average to zero.

## 5. Prior-art and falsification audit

The ingredients are not new individually. Jutila's zero-density theorem is classical literature; functional-equation mirror symmetry is classical; weighted Fourier/Beurling measure norms and Fourier-Stieltjes transforms are standard harmonic analysis; and the sharp one-pair contraction is already persisted as WI-395. A targeted prior-art search around zeta zero density combined with Paley--Wiener/weighted Fourier tests did not locate a theorem stating the density-normalized critical-projection consequence (1)--(3) or (14). Absence from that search is not treated as a priority claim. The durable claim here is the exact synthesis of previously established inputs.

The result can fail only if one of its explicit inputs or interfaces fails. A counterexample to the Jutila tail in the precise dyadic scaling (4), to WI-395's pointwise contraction (5), or to the functional-equation pairing would invalidate the proof. A test family with infinite `||mu||_(1/2)` lies outside the theorem. A source theorem that controls signed prime evaluation substantially below `||mu||_(1/2)` is not a counterexample; it is exactly the escape route the finding isolates.

## Research consequence

For the density-scale exceptional complement, stop treating the square-root-prime crossover as merely a fixed constant contraction. After zero density is inserted, the normalized scalar horizontal signal per unit absolute square-root Fourier budget tends to zero. The next useful arithmetic target is therefore not another positive portfolio or coherent scalar recombination inside the same absolute envelope. It is a genuinely signed source estimate whose gain over that envelope diverges on the defect-anchored family, or a change of observable that retains matrix/vertical/indefinite information. Keep sparse individual RH-failure detection as a separate problem: this finding does not touch that regime.

## Evidence status

- `LITERATURE+DERIVED`: Jutila's near-line zero-density theorem enters only through the already-audited dyadic consequence WI-029.
- `EXACT-DERIVED`: equations (1), (7)--(16) follow directly from WI-029 and the exact sharp contraction WI-395.
- `STRUCTURAL-BARRIER`: any scalar density-scale method charged by the componentwise absolute square-root-prime Fourier norm has vanishing horizontal sensitivity.
- `PRIOR-ART-AUDITED`: the constituent mechanisms are classical or already persisted; no priority claim is made for the synthesis.
