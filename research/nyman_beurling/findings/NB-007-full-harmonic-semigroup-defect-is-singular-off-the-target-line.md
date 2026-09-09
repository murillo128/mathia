# NB-007 — full harmonic semigroup defect is singular off the target line

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + FULL-ELL2-RIGIDITY + LOGARITHMIC-DIVERGENCE + NONUNIFORM-FINITE-DEPTH-BOUNDARY`. `NB-005` shows that the whole Bagchi semigroup identifies the Nyman target exactly, that every summable `p>2` defect norm is quantitatively noncoercive, and that each fixed nonzero projected Mellin alias has logarithmically divergent `ell^2` defect. `NB-006` then shows that this pointwise divergence is not uniform at finite depth: by retuning the Mellin frequency with the cutoff, the normalized truncated harmonic defect can be made arbitrarily small.

The missing full-`ell^2` statement is nevertheless exact and much stronger than the Mellin calculation. For **every** `h` in Bagchi's canonical discrete space `mathcal M`, put

\[
D_m h=(A_m^*-m^{-1/2}I)h,
\qquad
\mathcal E_X(h)=\sum_{m=2}^{X}\|D_mh\|^2.
\tag{1}
\]

Then

\[
\boxed{
\sum_{m=2}^{\infty}\|D_mh\|^2<\infty
\iff h\in\mathbb C e,
}
\tag{2}
\]

where `e=1` is the Nyman target. In fact every fixed non-target vector pays at least logarithmic cumulative defect. If

\[
c_n=n\int_0^{1/n}h(x)\,dx,
\qquad
\Gamma(h)=\sup_{n\ge1}\frac{|c_n-c_1|^2}{n},
\tag{3}
\]

then `Gamma(h)>0` exactly when `h` is not a scalar multiple of `e`, and

\[
\boxed{
\liminf_{X\to\infty}
\frac{\mathcal E_X(h)}{\log X}
\ge \frac14\Gamma(h).
}
\tag{4}
\]

Thus the nonsummable harmonic boundary left open by `NB-005` does not merely kill the particular Mellin aliases: the **untruncated** `ell^2` defect is an extended-valued singular selector, finite only on the target line. This does not solve the finite-section problem. The coefficient `Gamma(h)` has no uniform positive lower bound on the unit sphere of `e^perp`, and `NB-006` already shows that scale-dependent vectors can defeat every finite normalized cutoff. The viable question is therefore not whether the infinite harmonic sum identifies the target; it does, too violently. The live question is whether the **source-selected finite-section residuals** admit a uniform relation between `Gamma`, Mellin bandwidth, and an admissible truncated scale family.

## 1. Every semigroup defect exposes one multiplicative tail-average mismatch

Retain the exact real-space setup of `NB-004`. The canonical discrete space `mathcal M` consists of functions constant on

\[
I_n=\left(\frac1{n+1},\frac1n\right],
\qquad
\Phi_n=\mathbf1_{(0,1/n]},
\tag{5}
\]

and the total family `Phi_n` satisfies

\[
A_m\Phi_n=T_m\Phi_n=\sqrt m\,\Phi_{mn}.
\tag{6}
\]

For `h in mathcal M`, write

\[
F_n=\langle h,\Phi_n\rangle,
\qquad
c_n=nF_n.
\tag{7}
\]

Using (6), for every `m,n>=1`,

\[
\begin{aligned}
\langle D_mh,\Phi_n\rangle
&=\langle A_m^*h,\Phi_n\rangle
-m^{-1/2}\langle h,\Phi_n\rangle\\
&=\sqrt m\,F_{mn}-m^{-1/2}F_n\\
&=\boxed{
\frac{c_{mn}-c_n}{\sqrt m\,n}.}
\end{aligned}
\tag{8}
\]

Since

\[
\|\Phi_n\|^2=\frac1n,
\tag{9}
\]

Cauchy--Schwarz gives the exact one-coordinate lower bound

\[
\boxed{
\|D_mh\|^2
\ge
\frac{|c_{mn}-c_n|^2}{mn}.
}
\tag{10}
\]

This is the key point missed by looking only at Mellin eigenvectors. Every scale defect simultaneously measures how the normalized tail average `c_n` changes after the multiplicative refinement `n -> mn`.

For `n=1`, equation (10) becomes

\[
\boxed{
\|D_mh\|^2
\ge\frac{|c_m-c_1|^2}{m}.
}
\tag{11}
\]

Thus any finite full harmonic defect immediately forces the global sequence `c_m` to approach `c_1` in the harmonic square-summable sense. The remaining step is to compare that global control with the same statement viewed from an arbitrary base index `n`.

## 2. Finite full `ell^2` defect forces every tail average to equal the target average

Assume

\[
\sum_{m=2}^{\infty}\|D_mh\|^2<\infty.
\tag{12}
\]

Fix `n>=1`. Summing (10) over `m` gives

\[
\sum_{m=2}^{\infty}
\frac{|c_{mn}-c_n|^2}{m}
\le
n\sum_{m=2}^{\infty}\|D_mh\|^2
<\infty.
\tag{13}
\]

Equation (11), applied to all integer scales and then restricted to the subsequence `mn`, also gives

\[
\sum_{m=2}^{\infty}
\frac{|c_{mn}-c_1|^2}{m}
\le
n\sum_{k=2}^{\infty}
\frac{|c_k-c_1|^2}{k}
<\infty.
\tag{14}
\]

Let

\[
\Delta_n=c_n-c_1.
\]

For every `m`,

\[
|\Delta_n|^2
\le
2|c_n-c_{mn}|^2
+2|c_{mn}-c_1|^2.
\tag{15}
\]

Divide by `m` and sum over `m>=2`. The right-hand side is finite by (13)--(14), while the left is

\[
|\Delta_n|^2\sum_{m=2}^{\infty}\frac1m.
\]

The harmonic series diverges, so necessarily

\[
\boxed{c_n=c_1\qquad(n\ge1).}
\tag{16}
\]

`NB-004` gives the exact reconstruction of the value `h_n` of `h` on `I_n`:

\[
h_n=(n+1)c_n-nc_{n+1}.
\tag{17}
\]

Substituting (16) yields

\[
h_n=c_1
\qquad(n\ge1),
\]

hence

\[
\boxed{h=c_1e\quad\text{a.e.}}
\tag{18}
\]

Conversely the target covariance `A_m^*e=m^{-1/2}e` makes every `D_m` vanish on `Ce`. This proves (2).

The result is stronger than the exact joint-eigenspace theorem in `NB-005`. There one assumes every defect is exactly zero. Here each individual defect may be nonzero; merely asking their squared norms to be summable already forces all of them to vanish because the same tail averages are compared through infinitely many multiplicative refinements.

## 3. Every fixed non-target vector pays logarithmic cumulative defect

The same argument works before passing to infinity and gives a quantitative lower bound. Fix `n>=1`, let `M>=2`, and use (15). Equations (10)--(11) imply

\[
\frac{|c_{mn}-c_n|^2}{m}
\le n\|D_mh\|^2,
\tag{19}
\]

and

\[
\frac{|c_{mn}-c_1|^2}{m}
\le n\|D_{mn}h\|^2.
\tag{20}
\]

Therefore

\[
|c_n-c_1|^2
\sum_{m=2}^{M}\frac1m
\le
2n\sum_{m=2}^{M}\|D_mh\|^2
+2n\sum_{m=2}^{M}\|D_{mn}h\|^2.
\tag{21}
\]

Both sums on the right are contained in the cumulative scale range up to `nM`. Writing `H_M=sum_(m<=M)1/m`,

\[
\boxed{
\mathcal E_{nM}(h)
\ge
\frac{|c_n-c_1|^2}{4n}
\left(H_M-1\right).
}
\tag{22}
\]

Equivalently, for every `X>=2n`, with `M=floor(X/n)`,

\[
\boxed{
\mathcal E_X(h)
\ge
\frac{|c_n-c_1|^2}{4n}
\left(H_{\lfloor X/n\rfloor}-1\right).
}
\tag{23}
\]

For fixed `n`, `H_floor(X/n)=log X+O_n(1)`. Thus

\[
\liminf_{X\to\infty}
\frac{\mathcal E_X(h)}{\log X}
\ge
\frac{|c_n-c_1|^2}{4n}.
\tag{24}
\]

Taking the supremum over fixed `n` gives (4).

The gauge in (3) is finite. Indeed

\[
|c_n|
=n\left|\int_0^{1/n}h\right|
\le\sqrt n\,\|h\|,
\]

so `Gamma(h)<=4||h||^2`. It vanishes exactly when every `c_n=c_1`, which by (17) is exactly the target line. Hence every fixed non-target direction has a positive logarithmic divergence coefficient, although that coefficient can depend very badly on the direction.

## 4. The logarithmic coefficient is not a uniform distance modulus

The state dependence in `Gamma` is load-bearing. It cannot simply be replaced by a positive constant on the unit sphere of `e^perp` using the present argument.

For `N>=1`, define the two-shell vector

\[
g_N
=\frac N{\sqrt2}\mathbf1_{I_N}
-\frac{N+2}{\sqrt2}\mathbf1_{I_{N+1}}.
\tag{25}
\]

Since

\[
|I_N|=\frac1{N(N+1)},
\qquad
|I_{N+1}|=\frac1{(N+1)(N+2)},
\]

one checks exactly that

\[
\boxed{\|g_N\|=1,\qquad \langle g_N,e\rangle=0.}
\tag{26}
\]

Its normalized tail averages are especially sparse:

\[
c_n(g_N)=0\quad(n\ne N+1),
\qquad
c_{N+1}(g_N)=-\frac1{\sqrt2}.
\tag{27}
\]

Therefore

\[
\boxed{
\Gamma(g_N)=\frac1{2(N+1)}\longrightarrow0.
}
\tag{28}
\]

So the explicit coefficient in (4) does not itself give a uniform positive lower bound on all unit target-orthogonal vectors. This is compatible with `NB-006`, which is stronger in a different direction: there the vector is allowed to depend on the finite cutoff, and the **entire normalized truncated defect** can be made arbitrarily small by prime-log recurrence.

The distinction between fixed-vector asymptotics and finite-depth uniformity must therefore be preserved:

- every fixed non-target vector has at least logarithmically divergent cumulative harmonic defect by (4);
- the infimum over scale-dependent unit target-orthogonal vectors at a given finite depth can still tend to zero, as `NB-006` constructs explicitly.

No interchange of these quantifiers is justified.

## 5. Consequence for the Nyman finite-section route

`NB-005` left the harmonic `ell^2` boundary open because the projected Mellin aliases no longer had finite defect there. The present result closes that boundary completely for the **untruncated** semigroup observable: no alternative finite-energy alias exists. The full harmonic sum is finite exactly on the target line.

That is not yet the certificate the Nyman problem needs. As a finite-section observable it is actually too singular. Every non-target vector, however close to the target, has infinite full cost; while after truncation and normalization, `NB-006` shows that scale-dependent aliases can escape. Thus the useful interface lies between these two extremes.

For an actual best-approximation residual

\[
r_N=e-P_{V_N}e,
\]

one should now ask whether the source-selected geometry forces a quantitative lower bound on

\[
\Gamma(r_N)
=\sup_{n\ge1}
\frac{|n\int_0^{1/n}r_N-d_N^2|^2}{n},
\tag{29}
\]

where `c_1(r_N)=<r_N,e>=||r_N||^2=d_N^2`. A bound coupling this gauge to `d_N`, or to a controlled Mellin bandwidth of `r_N`, would turn (23) into a genuine finite-depth normalization theorem. Without such source information, (2) is exact identification but not a usable rate.

This sharpens the live alternative in `NB-006`. A positive continuation may prove a residual-specific inequality relating `Gamma(r_N)` to `d_N` and choose the scale cutoff accordingly; or it may abandon semigroup inference and control the exact target-aware Schur complement `1-b_N^*G_N^+b_N` directly. What is no longer open is whether the **infinite** harmonic semigroup defect itself has hidden finite-energy non-target directions.

## 6. Prior art and audit boundary

The only load-bearing external structure is Bagchi's canonical discrete subspace and integer dilation semigroup, already anchored in `research/nyman_beurling/SOURCES.md`. Equations (8)--(23) are elementary consequences of the exact relation `T_m Phi_n=sqrt(m) Phi_(mn)` and Hilbert-space Cauchy--Schwarz; no zero theorem, RH assumption, zeta moment, or Diophantine input enters them.

A targeted literature search over Nyman--Beurling dilation semigroups, joint/approximate eigenvectors, Mellin aliases, and semigroup defect/Dirichlet-form formulations located Bagchi's semigroup treatment, later operator reformulations such as Boqing Xue's 2019 preprint, and recent Gram/multiscale work, but did not locate the full harmonic-defect domain identity (2) or the logarithmic tail-average lower bound (23) as a named Nyman theorem. This is a prior-art boundary, not a blanket novelty claim; the proof is recorded in full so the statement does not depend on search absence.

Several controls prevent overreading. First, (4) is direction-dependent and does not contradict the finite-depth recurrence of `NB-006`. Second, the argument uses **all integer scales** in the full statement; a sparse scale subsequence may not have enough harmonic mass to force (16). Third, `Gamma(r_N)` is not bounded here, so no approximation rate for `d_N` follows. Fourth, the result concerns Bagchi's compressed canonical semigroup on `mathcal M`; it is not an abstract statement about every Nyman representation or every dilation system.

The result is unconditional and supplies no new zero-free region or RH implication. Its durable content is an exact classification of the nonsummable semigroup boundary and a new residual-specific quantity whose control would make the finite truncated certificate quantitative.