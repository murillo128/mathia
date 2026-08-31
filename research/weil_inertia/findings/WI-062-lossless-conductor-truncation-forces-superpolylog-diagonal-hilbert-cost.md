# WI-062 — lossless conductor truncation forces a super-polylogarithmic diagonal Hilbert cost

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE`, with a `LITERATURE+DERIVED` source bridge through WI-061 that retains WI-061's `NEEDS-AUDIT` boundary. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, change Mathia's current unconditional simple-critical proportion, or rule out a genuinely cross-conductor large-sieve/martingale theorem. It closes a narrower route left open by WI-060--WI-061: after doing the correct Parseval/Cauchy bookkeeping **inside each exact Fourier conductor**, Mikawa's modulus-weighted pair-AP square function still cannot be assembled across conductors by any argument that retains only the individual conductor Hilbert norms and the total Mikawa square-function budget.

The obstruction is exact and sharp at the information-interface level. For each retained conductor `d`, let `\mathcal K_d` be the finite booked shift family on which the conductor contribution is estimated and define

\[
B_d^*:=\sup_{k\in\mathcal K_d} B_d(h_1(k)),
\qquad
a_d:=d B_d^*,
\qquad
y_d:=d M_d,
\tag{1}
\]

where `B_d(h)` is the exact-support Fourier energy from WI-058 and `M_d` is the residue-maximal pair-error square sum from WI-061. Then the reduced-residue part of the one-conductor estimate has the form

\[
\|C_d\|_{\ell^2(k)}^2\le a_d y_d,
\qquad
\sum_{d\le Q}y_d\ll_A x^3(\log x)^{-A}.
\tag{2}
\]

From **only** this information, the optimal universal estimate for the scalar conductor sum is

\[
\boxed{
\left\|\sum_{d\in\mathcal D}C_d\right\|_2^2
\le
\left(\sum_{d\in\mathcal D}dB_d^*\right)
\left(\sum_{d\in\mathcal D}dM_d\right),
}
\tag{3}
\]

and the coefficient in front is best possible for abstract Hilbert vectors satisfying (2). But every raw `L^2` conductor truncation that captures asymptotically all of the `W`-local pair-main spectrum must have exponent `K(w)->infinity` by WI-059; for `d<=w^{K(w)}` this forces

\[
\boxed{
\sum_{d\le w^{K(w)}}dB_d^*
\gg_A (\log X)^A
\quad\text{for every fixed }A>0
}
\tag{4}
\]

at the source scale `w=(log X)^C`. Thus Mikawa's arbitrary **fixed** logarithmic saving cannot absorb the sharp norm-only cross-conductor cost. A successful repair must use mathematical information discarded by the diagonal conductor norms: genuine cross-conductor orthogonality/correlation, a vector-valued dispersion theorem, a martingale/Carleson structure, or a direct source-normalized covariance estimate.

## 1. Sharp abstract Hilbert-space assembly lemma

Let `H` be a Hilbert space, let `a_d>0`, `y_d>=0`, and suppose vectors `v_d in H` satisfy

\[
\|v_d\|_H^2\le a_d y_d,
\qquad
\sum_d y_d\le R.
\tag{5}
\]

Put

\[
S:=\sum_d a_d.
\tag{6}
\]

Then triangle inequality followed by Cauchy--Schwarz gives

\[
\begin{aligned}
\left\|\sum_d v_d\right\|_H
&\le \sum_d\|v_d\|_H\\
&\le \sum_d\sqrt{a_dy_d}\\
&\le \sqrt{\left(\sum_da_d\right)
               \left(\sum_dy_d\right)},
\end{aligned}
\]

hence

\[
\boxed{
\left\|\sum_dv_d\right\|_H^2\le SR.
}
\tag{7}
\]

This coefficient is **sharp given only (5)**. Fix a unit vector `u in H` and choose

\[
y_d=R\frac{a_d}{S},
\qquad
v_d=\sqrt{\frac RS}\,a_d u.
\tag{8}
\]

Then

\[
\|v_d\|_H^2
=\frac RSa_d^2
=a_dy_d,
\qquad
\sum_dy_d=R,
\]

while

\[
\left\|\sum_dv_d\right\|_H^2
=\left\|\sqrt{\frac RS}S u\right\|_H^2
=RS.
\tag{9}
\]

Therefore no proof that knows the family only through the diagonal norm caps and the total budget in (5) can replace `S` by a smaller universal coefficient. Any improvement must use relations among the vectors `v_d` themselves.

This lemma is elementary Hilbert-space geometry; no novelty is claimed for it.

## 2. Exact identification of the Mikawa/W-local diagonal data

WI-061 starts from the exact-conductor Fourier contribution

\[
C_d(k)
=
\sum_{\operatorname{cond}(b/d)=d}
\widehat G_{h_1(k)}(b/d)\,\widetilde T_{d,b}(h_2(k)).
\tag{10}
\]

Before the crude bound `dB_d<=6^{omega(d)}` is inserted, exact Parseval gives pointwise in the booked shift parameter

\[
|C_d(k)|^2
\le
B_d(h_1(k))\,d
\sum_{a\bmod d}
|\widetilde E_d(a,h_2(k))|^2.
\tag{11}
\]

Restrict first to the reduced-residue piece. For each retained `d`, let `\mathcal K_d` be the finite injective booked shift subfamily to which the WI-061 estimate is applied and set

\[
B_d^*:=\sup_{k\in\mathcal K_d}B_d(h_1(k)).
\tag{12}
\]

The booking makes `k\mapsto h_2(k)` injective on `\mathcal K_d`, but does not require `h_1(k)` to be constant. Summing (11) only after taking the finite-family supremum gives

\[
\begin{aligned}
\|C_d\|_{\ell^2(k)}^2
&\le dB_d^*
   \sum_{k\in\mathcal K_d}
   \sum_{(a,d)=1}|E_d(a,h_2(k))|^2\\
&\le dB_d^*\,\varphi(d)M_d\\
&\le d^2B_d^*M_d,
\end{aligned}
\tag{13}
\]

where

\[
M_d:=\max_{(a,d)=1}
\sum_{0<2k\le x}|E(x;d,a,2k)|^2.
\tag{14}
\]

Consequently

\[
\boxed{
\|C_d\|_{\ell^2(k)}^2
\le d^2B_d^*M_d
=\bigl(dB_d^*\bigr)\bigl(dM_d\bigr).
}
\tag{15}
\]

This is (5) with

\[
a_d=dB_d^*,
\qquad y_d=dM_d.
\tag{16}
\]

The square-function extracted in WI-061 from Mikawa's proof supplies, in its stated range,

\[
\boxed{
\sum_{d\le Q}dM_d
\ll_A x^3(\log x)^{-A}
}
\tag{17}
\]

for every fixed `A>0`, with the corresponding fixed `B(A)` in
`Q<=x^(1/2)(log x)^(-B(A))`.

The non-reduced residue classes from WI-061 are deliberately omitted here. They contribute a separately bounded prime-power error and cannot rescue an obstruction already present in the optimistic reduced-only problem. Likewise, replacing the shift-dependent `dB_d(h_1(k))` uniformly by the rougher `6^omega(d)` is unnecessary and would only weaken the diagnostic.

Applying the sharp lemma gives exactly (3).

## 3. The booked-family conductor weight `d B_d^*` is never small on an active exact support

WI-058 gives, for odd squarefree exact conductor `d` and every locally admissible shift `h`,

\[
B_d(h)=\prod_{p\mid d}v_p(h),
\tag{18}
\]

with

\[
v_p(h)=
\begin{cases}
1/(p-1),&p\mid h,\\[1mm]
2/(p-2),&p\nmid h.
\end{cases}
\tag{19}
\]

Hence

\[
dB_d(h)
=
\prod_{p\mid d}p\,v_p(h).
\tag{20}
\]

For every active odd prime,

\[
pv_p(h)
=
\begin{cases}
p/(p-1)>1,&p\mid h,\\[1mm]
2p/(p-2)>2,&p\nmid h.
\end{cases}
\tag{21}
\]

and therefore, uniformly in the shift,

\[
\boxed{dB_d(h)\ge1.}
\tag{22}
\]

Taking the supremum over the finite booked family preserves this bound:

\[
\boxed{dB_d^*\ge1.}
\tag{23}
\]

Primes dividing the shift only weaken the local factor from `>2` to `>1`; they do not remove the lower bound. Finitely many local primes pinned by a source progression can be deleted exactly as in WI-058 without changing the asymptotic conclusion below.

Let `P_w` be the number of active odd primes up to `w`. In the full Yang power-coefficient regime audited in WI-059, `P_w=pi(w)+O(1)`. For any integer `k>=0`, every support set of at most `k` active primes has conductor at most `w^k`. Thus

\[
\boxed{
S_w(w^K):=
\sum_{\substack{d\mid W\\d\le w^K}}dB_d^*
\ge
\sum_{j=0}^{\lfloor K\rfloor}\binom{P_w}{j}.
}
\tag{24}
\]

This lower bound uses only the exact local Fourier-energy law and its shift-uniform local factor bound. No prime-pair theorem enters it.

## 4. Every asymptotically lossless raw `L^2` cutoff makes the diagonal cost super-polylogarithmic

WI-059 proves the exact qualitative threshold for raw Fourier-energy truncations

\[
D_w=w^{K(w)}:
\qquad
\nu_{W,h}\{d>D_w\}\to0
\quad\Longleftrightarrow\quad
K(w)\to\infty
\tag{25}
\]

on the full active product. In particular, making the discarded **absolute** local-main `L^2` energy `o(1)` also forces `K(w)->infinity`, since the total energy is bounded below by a positive multiple of `log w`.

Assume therefore that `K(w)->infinity`. Set

\[
k(w):=\min\!\left(
\lfloor K(w)\rfloor,
\lfloor\sqrt{P_w}\rfloor
\right).
\tag{26}
\]

Then `k(w)->infinity`, `k<=K`, and `k=o(P_w)`. From (24),

\[
S_w(w^{K(w)})
\ge\binom{P_w}{k}.
\tag{27}
\]

Using

\[
\binom Pk
\ge
\left(\frac{P-k+1}{k}\right)^k,
\tag{28}
\]

and `k<=sqrt(P)`, for all large `w` one has

\[
\log\binom{P_w}{k}
\ge
k\left(\frac12\log P_w+O(1)\right).
\tag{29}
\]

Since `P_w~w/log w`,

\[
\log P_w=(1+o(1))\log w,
\]

so

\[
\boxed{
\log S_w(w^{K(w)})
\ge
\left(\frac12+o(1)\right)k(w)\log w.
}
\tag{30}
\]

At the Shao--Teräväinen/Yang scale

\[
w=(\log X)^C,
\tag{31}
\]

with fixed `C>0`, this becomes

\[
\frac{\log S_w(w^{K(w)})}{\log\log X}
\ge
\left(\frac C2+o(1)\right)k(w)
\longrightarrow\infty.
\tag{32}
\]

Therefore, for **every** fixed `A>0`, not merely at WI-059's convenient explicit sufficient cutoff,

\[
\boxed{
\frac{S_w(w^{K(w)})}{(\log X)^A}
\longrightarrow\infty.
}
\tag{33}
\]

The conclusion is stronger than using the particular
`K=(2+eta)log log w/log log log w`: every growing-exponent cutoff required for asymptotically lossless raw `L^2` capture already forces a conductor-diagonal Hilbert cost larger than every fixed power of `log X`.

## 5. Why Mikawa's arbitrary fixed logarithmic saving does not close this route

For every **fixed** `A`, WI-061's Mikawa bridge supplies the budget (17), with a corresponding fixed modulus-range parameter `B(A)`. The retained conductors `w^{K(w)}=X^{o(1)}` remain below the square-root modulus range for the explicit WI-059 cutoffs and for any comparable subpolynomial truncation used by this route.

But (3) and (33) show that the norm-only assembly gives at best

\[
\left\|\sum_d C_d\right\|_2^2
\ll_A
x^3(\log x)^{-A}
S_w(D_w),
\tag{34}
\]

where `S_w(D_w)` dominates every fixed power of `log X`. Choosing a larger **fixed** `A` never resolves that asymptotic mismatch. Choosing `A=A(X)->infinity` is not licensed by Mikawa's theorem as stated, because its constants and admissible `B(A)` depend on the fixed parameter `A` with no required uniformity in a growing `A`.

Thus the chain

\[
\boxed{
\text{exact-support Parseval}
\to
\text{one-conductor Mikawa }L^2
\to
\text{diagonal conductor norms}
\to
\text{Cauchy across }d
}
\tag{35}
\]

cannot close the welding covariance while retaining asymptotically all of the deterministic `W`-local `L^2` spectrum.

The sharpness construction (8)--(9) matters here. This is not merely a poor choice of Cauchy weights: **no universal inequality derived solely from those diagonal norm caps and their total budget can do better.**

## 6. Relation to WI-060 and WI-061

WI-060 proves a mode-level obstruction: the retained Fourier family has super-polylogarithmic Wiener `l^1` mass, so a fixed-log estimate for every additive mode followed by absolute summation cannot work.

The present obstruction is different and strictly later in the proposed repair. It grants the improvement that WI-060 asked for:

1. group all Fourier modes with the same exact conductor;
2. use exact Parseval inside that conductor;
3. apply the conditioned pair-AP square function from WI-061;
4. keep only one Hilbert norm per conductor.

Even after those steps, discarding cross-conductor geometry leaves the sharp coefficient

\[
S_w(D)=\sum_{d\le D}dB_d^*,
\]

which is again super-polylogarithmic at every asymptotically lossless raw `L^2` cutoff.

This makes WI-061's open phrase “cross-conductor square-function / martingale assembly” more precise. A successful theorem cannot merely be a diagonal square sum over conductors followed by an abstract Hilbert-space inequality. It must see some **off-diagonal relation among conductors** before scalarization: orthogonality of arithmetic projections, a vector-valued large sieve, martingale differences, conductor nesting/cancellation, or a direct pair-error covariance theorem.

## 7. Stress tests and scope

Several stronger interpretations are false and are excluded.

- This does **not** prove that the actual arithmetic vectors `C_d(k)` are aligned. Equation (9) is an abstract extremizer showing that alignment cannot be excluded from the diagonal data alone. Arithmetic cross-conductor orthogonality may exist; proving it is precisely the remaining positive route.
- This does **not** rule out large-sieve or Carleson inequalities whose hypotheses use the actual character/congruence structure before the `d`-components are reduced to norms. Such an inequality would add information absent from (5).
- This does **not** rule out a direct vector-valued strengthening of Mikawa that estimates the desired conductor sum before Cauchy--Schwarz. WI-061 only extracts the diagonal modulus-weighted square budget from the printed proof.
- This does **not** reopen the fixed-polylog truncation. WI-059 already proves that any fixed `K` discards a positive relative fraction of the deterministic local-main `L^2` energy.
- The non-reduced residue prime-power term is not used to manufacture the obstruction. It is omitted optimistically; adding a nonnegative error budget cannot improve the diagonal-information ceiling.
- The conclusion is about the `W`-local/Yang welding repair and does not create a general barrier for all matrix-inertia or Weil-form improvements.

A possible escape based on a much smaller cutoff must first defeat WI-059's necessity `K(w)->infinity` for asymptotically lossless raw `L^2` capture, or use a different norm/approximation mechanism in which the discarded spectrum is harmless for reasons stronger than its own `L^2` mass.

## 8. Prior-art and novelty audit

The abstract lemma (5)--(9) is ordinary Hilbert-space triangle inequality and Cauchy--Schwarz with its equality case. The local factorization (18)--(23), conductor-energy threshold (25), and source scale (31) are already persisted in WI-058--WI-060. The arithmetic budget (17) is the source-specific consequence extracted in WI-061 from H. Mikawa, *On prime twins in arithmetic progressions*, *Tsukuba Journal of Mathematics* 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`, primary open-access source `https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf`.

A targeted prior-art check around Barban--Davenport--Halberstam square means, large-sieve/Hilbert-space assembly, and Mikawa's pair-AP dispersion found the standard square-mean and large-sieve frameworks, but no theorem was imported that supplies the **off-diagonal cross-conductor structure** missing here. No novelty is claimed for Cauchy--Schwarz, large-sieve philosophy, conductor decompositions, or the individual literature inputs, and absence of this exact Yang/`W`-local formulation in the searched literature is not a priority claim.

The durable Mathia contribution is the exact source-specific information-interface calculation: combine WI-058's shift-uniform `dB_d(h)\ge1` local energy law with WI-059's necessary growing cutoff and WI-061's `dM_d` budget, compute the sharp norm-only assembly constant using the booked-family coefficient `dB_d^*`, and show that it is super-polylogarithmic for every lossless raw `L^2` truncation.

## 9. Consequence for the live research direction

The shortest credible continuation after WI-061 is now narrower:

\[
\boxed{
\text{do not search for a better diagonal Cauchy weight across conductors;}\\
\text{search for a theorem that preserves cross-conductor arithmetic geometry.}
}
\tag{36}
\]

Concrete positive targets include a vector-valued form of Mikawa/Linnik dispersion in which the exact-conductor projections remain orthogonal until after the modulus sum, a martingale-difference decomposition tied to the CRT prime filtration, or a direct estimate for the `W`-localized pair covariance before its Fourier conductors are scalarized.

A decisive falsification test for any proposed repair is therefore: after all deterministic/source weights are restored, identify the exact bilinear or quadratic form that couples `d` and `d'` and prove a saving unavailable from the diagonal bounds (15)/(17). If the proof can be rewritten using only `\|C_d\|_2` and `\sum dM_d`, the sharp extremizer above shows that it has not crossed the barrier.