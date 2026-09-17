# PC-329 — no fixed packet deflation bounds the canonical Green family

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `PRIOR-ART-CLASSICALIZATION` for the finite PNT/Li deflation route left open by PC-328.

PC-328 shows that the canonical prime-support Green operator has band-normalized outliers forced already by fixed Fourier modes of size `1/log q`, and leaves open the natural repair of subtracting or deflating a finite low-frequency PNT/Li packet before looking for a zero-sensitive residual.

That repair cannot work if the packet complexity stays fixed. There are two distinct interpretations of a finite packet, and both fail:

1. changing or neutralizing any fixed number of periodic source Fourier residues leaves another untouched fixed residue with the same PNT-scale amplitude;
2. even allowing an arbitrary conductor-dependent operator correction of fixed rank, the finite low-frequency Cauchy block has full rank and cannot be approximated away below the same PNT scale.

More precisely, for every fixed integer `R>=0` there is `kappa_R>0` such that, for distinct primes `q,r -> infinity`, any canonical Green family after either kind of fixed-complexity deflation still satisfies a normalized operator-norm lower bound of order

\[
\boxed{
\kappa_R\,
\frac{\sqrt{qr}}
{(\log q\,\log r)^{3/2}}.
}
\tag{1}
\]

For comparable conductors `q asymp r asymp Q`, this is `Omega_R(Q/(log Q)^3)`, the same conductor/logarithm order as the raw PC-328 obstruction. Thus a bounded growing-conductor residual cannot be obtained by freezing a finite low-mode packet. Any viable deflation must have complexity growing with the conductor, or subtract a genuinely full source profile rather than finitely many modes/channels.

## 1. Every fixed canonical Fourier mode carries a nonzero PNT coefficient

Retain the canonical source and Fourier convention of PC-328. For prime `q`, put

\[
L_q:=\log q,
\qquad
P_q=\{p:2<p<q,\ p\text{ prime}\},
\qquad
R_q=|P_q|,
\]

and, for `h not congruent to 0 (mod q)`,

\[
a_q(h)=\frac1{R_q}\sum_{p\in P_q}e^{-2\pi i hp/q}.
\tag{2}
\]

PC-328 derives from the quantitative prime number theorem and partial summation that, for every fixed integer `h>=1`,

\[
\boxed{
a_q(h)=\frac{C_h}{L_q}+O_h(L_q^{-2}),}
\qquad
C_h=-\int_0^1e^{-2\pi iht}\log t\,dt.
\tag{3}
\]

The only additional point needed here is that **none of the constants `C_h` vanish**. Taking real parts and integrating by parts gives

\[
\operatorname{Re}C_h
=
\frac1{2\pi h}
\int_0^{2\pi h}\frac{\sin u}{u}\,du
=
\frac{\operatorname{Si}(2\pi h)}{2\pi h}.
\tag{4}
\]

For integer `h>=1`, split the sine integral into the `h` successive intervals `[2\pi j,2\pi(j+1)]`. On each interval the positive half-wave precedes the negative half-wave and has the smaller denominator. After translating both halves to `[0,\pi]`, their sum is

\[
\int_0^\pi \sin v
\left(
\frac1{2\pi j+v}
-
\frac1{(2j+1)\pi+v}
\right)dv>0.
\tag{5}
\]

Hence `Si(2 pi h)>0`, so

\[
\boxed{C_h\neq0\quad\text{for every fixed }h>=1.}
\tag{6}
\]

The low-frequency PNT background is therefore not carried by one exceptional mode such as `h=1`; it is an infinite fixed-mode ladder.

## 2. Any fixed number of source-residue edits leaves a PNT-scale outlier

Fix `R`. Let `\widetilde a_q` be obtained from the canonical periodic source `a_q` by changing at most `R` residue values modulo `q`, with the changed values uniformly bounded as `q->infinity`. This includes zeroing, subtracting, or replacing any fixed collection of low Fourier residues by a bounded PNT/Li reference. Define `\widetilde b_r` similarly.

Among the `R+1` residues

\[
1,2,\ldots,R+1,
\]

at least one, say `h_q`, is untouched. Since this is a fixed finite set, (3) and (6) give a constant `d_R>0` such that, for all sufficiently large `q`,

\[
|\widetilde a_q(h_q)|=|a_q(h_q)|\ge\frac{d_R}{L_q}.
\tag{7}
\]

Likewise there is `k_r in {1,...,R+1}` with

\[
|\widetilde b_r(k_r)|\ge\frac{d_R}{L_r}.
\tag{8}
\]

The corresponding cross-level Green operator is

\[
\widetilde X_{q,r}(k,l)
=
\frac{\widetilde a_q(k)\widetilde b_r(l)}{k+l}.
\tag{9}
\]

Testing the single untouched matrix coefficient gives

\[
\boxed{
\|\widetilde X_{q,r}\|
\ge
\frac{d_R^2}{2(R+1)L_qL_r}.
}
\tag{10}
\]

The intrinsic Hilbert-band scale is stable under these fixed-cardinality edits. Indeed the canonical RMS quantity from PC-323/PC-328 is

\[
\mu_q=\frac1q\sum_{j=1}^{q-1}|a_q(j)|^2
\sim\frac{L_q}{q}.
\tag{11}
\]

Changing at most `R` uniformly bounded residues changes this average by only `O_R(1/q)`, so

\[
\widetilde\mu_q
=\mu_q+O_R(q^{-1})
\sim\frac{L_q}{q},
\qquad
\widetilde\mu_r
\sim\frac{L_r}{r}.
\tag{12}
\]

Therefore the edited Hilbert-band scale

\[
\widetilde c_{q,r}
:=\sqrt{\widetilde\mu_q\widetilde\mu_r}
\sim
\sqrt{\frac{L_qL_r}{qr}}
\tag{13}
\]

and (10) imply

\[
\boxed{
\frac{\|\widetilde X_{q,r}\|}{\widetilde c_{q,r}}
\ge
\kappa_R
\frac{\sqrt{qr}}{(L_qL_r)^{3/2}}
(1+o(1)).
}
\tag{14}
\]

Thus removing finitely many periodic Fourier channels does not merely fail to prove tightness: it leaves operator norm escaping at the same `sqrt(qr)/(log q log r)^(3/2)` scale as PC-328.

## 3. Arbitrary fixed-rank operator subtraction also fails

The previous argument uses the source representation. A stronger operator-level statement rules out the possibility that a clever rank-`R` correction could cancel the low-mode obstruction without corresponding to residue deletion.

Put

\[
m:=R+1
\]

and let `P_m` denote projection onto the first `m` coordinates of `ell^2(N)`. For the original canonical operator `X_{q,r}`, define its fixed low-frequency compression

\[
B_{q,r}^{(m)}:=P_mX_{q,r}P_m.
\tag{15}
\]

By the fixed-mode asymptotic (3), uniformly on this fixed `m x m` block,

\[
L_qL_r B_{q,r}^{(m)}
\longrightarrow
M_m,
\qquad
(M_m)_{kl}=\frac{C_kC_l}{k+l},
\quad 1\le k,l\le m.
\tag{16}
\]

Write

\[
M_m=D_C H_mD_C,
\qquad
D_C=\operatorname{diag}(C_1,\ldots,C_m),
\qquad
(H_m)_{kl}=\frac1{k+l}.
\tag{17}
\]

Equation (6) makes `D_C` invertible. The finite Hilbert matrix `H_m` is a Cauchy matrix and is invertible. Hence `M_m` is invertible, and its least singular value

\[
s_m(M_m)=:\sigma_R>0
\tag{18}
\]

is a fixed positive constant depending only on `R`. By continuity of singular values, for all sufficiently large `q,r`,

\[
s_m(B_{q,r}^{(m)})
\ge
\frac{\sigma_R}{2L_qL_r}.
\tag{19}
\]

Now let `K_{q,r}` be **any** operator of rank at most `R`; it may depend arbitrarily on the conductors. Its compression `P_mK_{q,r}P_m` still has rank at most `R=m-1`. The finite-dimensional Schmidt/Eckart--Young--Mirsky theorem therefore gives

\[
\begin{aligned}
\|X_{q,r}-K_{q,r}\|
&\ge
\|P_m(X_{q,r}-K_{q,r})P_m\|\\
&\ge
s_m(B_{q,r}^{(m)})\\
&\ge
\frac{\sigma_R}{2L_qL_r}.
\end{aligned}
\tag{20}
\]

Dividing by the canonical Hilbert-band scale `c_{q,r}~sqrt(L_qL_r/(qr))` yields

\[
\boxed{
\inf_{\operatorname{rank}K\le R}
\frac{\|X_{q,r}-K\|}{c_{q,r}}
\ge
\frac{\sigma_R}{2}
\frac{\sqrt{qr}}{(L_qL_r)^{3/2}}
(1+o(1)).
}
\tag{21}
\]

For the canonical self-adjoint dilation, subtracting the off-diagonal dilation of `K` gives the same operator norm. Such a correction is finite rank and therefore does not alter the essential Hilbert band from PC-323. So no optimally chosen fixed-rank spectral packet can produce a bounded band-normalized residual either.

## 4. What this does and does not close

PC-328 left finite low-mode PNT/Li deflation as the first natural normalization test. Equations (14) and (21) close both fixed-complexity versions of that test:

\[
\boxed{
\text{fixed number of source Fourier channels}
\quad\text{or}\quad
\text{fixed operator rank}
\quad\Longrightarrow\quad
\text{PNT-scale escape survives}.
}
\tag{22}
\]

This is a stronger obstruction than merely saying that the universal PC-327 Schatten defect remains. The canonical low-frequency background itself cannot be reduced to a finite packet in the growing-conductor limit.

The result does **not** rule out a deflation rank growing with `q,r`, nor subtraction of a full conductor-dependent Li/PNT source profile. Those are genuinely different limits. In particular, the theorem gives no lower bound on the minimal growing rank needed for tightness and says nothing yet about whether a fully Li-subtracted residual becomes zero-sensitive.

That is now the correct next boundary: a surviving program must renormalize an increasing family of PNT modes or a complete smooth reference before asking whether the remaining nonlocal spectral data carry information beyond classical prime-density asymptotics and the PC-325 phase/autocorrelation quotient.

## 5. Prior-art and novelty audit

The ingredients are classical. The fixed-mode estimate (3) is the quantitative prime number theorem plus Stieltjes partial summation already audited in PC-328 and anchored through the Montgomery--Vaughan PNT literature used earlier in this line. Invertibility of `H_m` is the elementary Cauchy/Hilbert determinant fact. Equation (20) is the classical Schmidt/Eckart--Young--Mirsky best-low-rank approximation theorem.

A targeted prior-art search across prime exponential sums/major-arc Fourier asymptotics, finite Hilbert matrices, and low-rank approximation found these expected component theories, but no theorem packaging the canonical centered prime-support DFT, the Prime-Circle cross-level Green kernel, its intrinsic Hilbert-band normalization, and fixed-complexity deflation into (14) or (21). The novelty claim is therefore deliberately project-local: this is a new **no-go consequence for the Prime-Circle Green architecture**, not a new theorem about the prime number theorem, Hilbert matrices, or low-rank approximation.

The arithmetic interpretation is negative as well. The obstruction uses only the smooth PNT coefficients `C_h`; no explicit formula or zeta zero enters. Smooth Li-type controls inherit the same fixed-mode leading packet. Thus survival of the outliers after finite deflation is background prime-density geometry, not evidence for RH.

## 6. Falsification hooks

This finding should be revised or withdrawn if any of the following occurs:

1. the canonical Fourier normalization of PC-328 is shown not to satisfy the fixed-mode asymptotic (3);
2. some `C_h` in the finite low-frequency ladder vanishes, contradicting (4)--(6);
3. the Green kernel used in PC-323 is shown not to contain the fixed compression (15);
4. the intrinsic essential-band scale differs from `sqrt(mu_q mu_r)` for the edited or canonical periodic sources considered here;
5. a proposed deflation is shown to have conductor-growing rank or to modify a full periodic source profile, in which case it lies outside the fixed-complexity theorem rather than falsifying it.

Absent such a failure, the durable conclusion is exact: **a frozen finite PNT/Li packet cannot renormalize the canonical growing-conductor Green family; the amount of background that must be removed necessarily grows with the conductor.**