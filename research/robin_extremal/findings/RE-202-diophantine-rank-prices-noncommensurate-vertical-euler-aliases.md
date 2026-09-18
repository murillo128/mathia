# RE-202 — Diophantine rank prices noncommensurate vertical Euler aliases

**Status:** `EXACT-DERIVED + COMPLEX-EULER-SAMPLING + SIMULTANEOUS-DIOPHANTINE-RECURRENCE + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + KV-FIDELITY + INTEGER-MULTIPLICITIES + SPECTRAL-RANK-BOUNDARY`.

**Parent findings:** RE-200, RE-201.

`RE-201` shows that the commensurate DFT panel from `RE-200` has an exact multiplicative shell alias. The natural escape is to break the common period by using incommensurate or jittered imaginary heights. That does remove the exact identity, but it does not remove cheap **approximate** shell recurrences unless the sampling set has enough Diophantine complexity.

Put

\[
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\qquad
d_Q:=\frac1{\sqrt Q\log Q},
\tag{1}
\]

and define the convenient KV-safe logarithmic displacement scale

\[
\mathcal L_Q
:=(\log Q)^{5/3}(\log\log Q)^{1/3}.
\tag{2}
\]

The role of `\mathcal L_Q` is only sufficient, not claimed sharp: if a remote multiplicative shift `\Lambda=e^L` satisfies

\[
L=o(\mathcal L_Q),
\tag{3}
\]

then at the remote scale `X\asymp \Lambda Q` one has

\[
V(X)=o(\log Q).
\tag{4}
\]

Consequently the selector-size prime packet used below remains below every fixed Korobov--Vinogradov source envelope.

Now fix an integer `r>=1` and real base frequencies `\omega_1,\ldots,\omega_r` of bounded size. Let the sampled heights lie in the rank-`r` integer module

\[
\mathcal T_Q\subset
\left\{
\sum_{\nu=1}^r n_\nu\omega_\nu:
 n_\nu\in\mathbb Z,
 \sum_{\nu=1}^r|n_\nu|\le K
\right\}.
\tag{5}
\]

No rational relation among the `\omega_\nu` is assumed. If

\[
K^r=o(\mathcal L_Q),
\tag{6}
\]

then there are disjoint finite sets of ordinary primes `P_Q,R_Q`, with coefficient `+1` on `P_Q` and `-1` on `R_Q`, and a multiplicative displacement `\Lambda=e^L` such that:

1. `P_Q` lies in one fixed selector-scale multiplicative shell, `|P_Q|\asymp \sqrt Q/\log Q`, and

\[
\sum_{q\in P_Q}H_q(1)=\Theta(d_Q),
\qquad
H_q(s):=\log(1-q^{-s})^{-1}.
\tag{7}
\]

2. `R_Q` lies in a translated remote shell at scale `\Lambda Q`, with

\[
L=\log\Lambda=o(\mathcal L_Q).
\tag{8}
\]

3. For

\[
D_Q(s):=
\sum_{q\in P_Q}H_q(s)-
\sum_{q\in R_Q}H_q(s),
\tag{9}
\]

one has

\[
\boxed{
\max_{t\in\mathcal T_Q}|D_Q(1+it)|=o(d_Q).
}
\tag{10}
\]

4. Starting from ordinary prime multiplicity one, the perturbation uses only multiplicities `{0,1,2}` and, for every fixed `b>0`, obeys

\[
|\Delta\vartheta(x)|
=o\!\left(xe^{-bV(x)}\right)
\tag{11}
\]

on and beyond the affected scales.

Thus **finite spectral incommensurability is not itself a shell-index discriminator**. What matters is the Diophantine rank of the height family and the approximation denominator needed before the source-fidelity budget runs out.

A concrete consequence is already strong. For two incommensurate arithmetic panels (`r=2`), the same selector-scale alias survives whenever

\[
\boxed{
K=o\!\left(
(\log Q)^{5/6}(\log\log Q)^{1/6}
\right).
}
\tag{12}
\]

At the opposite architectural extreme, take an arbitrary collection of `M` heights with `\max |t_j|=O(M)` and no low-rank module assumption. Treating the heights themselves as `M` generators gives a universal recurrence whenever

\[
M=o(\log\mathcal L_Q)=o(\log\log Q).
\tag{13}
\]

Hence **every** such fully jittered sub-`log log Q` panel still admits a selector-scale ordinary-prime remote alias at KV-safe distance.

## 1. Simultaneous approximation gives a quantitative shell recurrence

The only approximation input needed is the elementary simultaneous Dirichlet pigeonhole argument, which we reproduce so that no external theorem is load-bearing.

For real numbers `\alpha_1,\ldots,\alpha_r` and an integer `N>=2`, consider

\[
0,\alpha,2\alpha,\ldots,N^r\alpha
\pmod{\mathbb Z^r}
\tag{14}
\]

inside the unit `r`-cube, where `\alpha=(\alpha_1,\ldots,\alpha_r)`. Partition the cube into `N^r` boxes of side `1/N`. Two of the `N^r+1` points lie in the same box, so for some integer `1<=\ell<=N^r`,

\[
\max_{1\le\nu\le r}
\|\ell\alpha_\nu\|_{\mathbb R/\mathbb Z}
\le\frac1N.
\tag{15}
\]

Apply this with

\[
\alpha_\nu=\frac{\omega_\nu}{2\pi}.
\tag{16}
\]

Choose a parameter `A=A_Q->infinity` and take

\[
N=\lceil KA\rceil.
\tag{17}
\]

After multiplying `\ell` by one fixed integer if necessary, we may also require the logarithmic displacement `L` to exceed a fixed constant so that the local and remote prime shells are disjoint. This changes only absolute constants. Then

\[
L\ll_r (KA)^r
\tag{18}
\]

and, for every sampled height `t` in (5),

\[
\begin{aligned}
\left\|\frac{tL}{2\pi}\right\|_{\mathbb R/\mathbb Z}
&\le
\sum_{\nu=1}^r|n_\nu|
\left\|\frac{\omega_\nu L}{2\pi}\right\|_{\mathbb R/\mathbb Z}\\
&\ll_r \frac K N
\ll_r \frac1A.
\end{aligned}
\tag{19}
\]

Therefore

\[
\boxed{
\max_{t\in\mathcal T_Q}
|e^{-itL}-1|
\ll_r A^{-1}.
}
\tag{20}
\]

Under (6), take for example

\[
A=
\left(
\frac{\mathcal L_Q}{K^r}
\right)^{1/(2r)}.
\tag{21}
\]

Then `A->infinity` and

\[
(KA)^r
=\sqrt{K^r\mathcal L_Q}
=o(\mathcal L_Q),
\tag{22}
\]

so (18) gives exactly the KV-safe displacement (8), while (20) is `o(1)`.

Equation (12) is simply (6) with `r=2`. Notice that irrationality of `\omega_1/\omega_2` is irrelevant to the upper bound: it destroys an exact common period but simultaneous approximation recreates an approximate one before the permitted repair distance is exhausted.

For a completely arbitrary `M`-point panel, use the `M` heights themselves as generators with coefficient radius one. Taking

\[
A=\mathcal L_Q^{1/(2M)}
\tag{23}
\]

gives an approximation denominator at most `A^M=\sqrt{\mathcal L_Q}` and phase error `O(A^{-1})`. The error tends to zero precisely when `M=o(\log\mathcal L_Q)`, which yields (13). This corollary makes no arithmetic-grid assumption at all.

## 2. The recurrence pulls back to exact ordinary-prime Euler atoms

It remains to show that the phase recurrence is not merely a formal trigonometric alias. Let `a>0` be the constant in the already anchored KV PNT input

\[
\vartheta(X)=X+O(Xe^{-aV(X)}).
\tag{24}
\]

Choose a fixed local center `X_0=2Q` and put

\[
B:=\left\lfloor c\frac{\sqrt Q}{\log Q}\right\rfloor
\tag{25}
\]

for any fixed `c>0`. Let

\[
\eta_0=e^{-aV(X_0)/2}.
\tag{26}
\]

The logarithmic interval

\[
I_0=[X_0e^{-\eta_0},X_0e^{\eta_0}]
\tag{27}
\]

contains `\gg \eta_0X_0/\log X_0` ordinary primes, which is much larger than `B`. Choose any `B` distinct primes there and call the set `P_Q`.

Now set

\[
\Lambda=e^L,
\qquad
X_1=\Lambda X_0,
\qquad
\eta_1=e^{-aV(X_1)/2}.
\tag{28}
\]

Because `L=o(\mathcal L_Q)`, (4) holds. In particular

\[
\eta_1\sqrt Q\,\frac{\log Q}{\log X_1}
=Q^{1/2-o(1)}\frac{\log Q}{\log X_1}
\longrightarrow\infty.
\tag{29}
\]

Thus the remote interval

\[
I_1=[X_1e^{-\eta_1},X_1e^{\eta_1}]
\tag{30}
\]

contains enough ordinary primes to choose

\[
C:=\lfloor \Lambda B\rceil
\tag{31}
\]

distinct members. Call that set `R_Q`.

Let

\[
T_Q:=\max_{t\in\mathcal T_Q}|t|.
\tag{32}
\]

For the rank-`r` panel in (5), `T_Q=O_r(K)`; for the arbitrary-panel corollary we assumed `T_Q=O(M)`. Both are polylogarithmic on the stated ranges, hence

\[
T_Q\eta_0+T_Q\eta_1=o(1).
\tag{33}
\]

Uniformly for `t\in\mathcal T_Q`, the first Euler harmonics therefore satisfy

\[
\sum_{q\in P_Q}q^{-1-it}
=
B X_0^{-1-it}
\left(1+O(T_Q\eta_0+\eta_0)\right),
\tag{34}
\]

and

\[
\sum_{r\in R_Q}r^{-1-it}
=
C X_1^{-1-it}
\left(1+O(T_Q\eta_1+\eta_1)\right).
\tag{35}
\]

Since `C=\Lambda B+O(1)` and `X_1=\Lambda X_0`, equations (20), (34) and (35) give

\[
\max_{t\in\mathcal T_Q}
\left|
\sum_{q\in P_Q}q^{-1-it}
-
\sum_{r\in R_Q}r^{-1-it}
\right|
\ll
\frac BQ
\left(
A^{-1}
+T_Q\eta_0+T_Q\eta_1
+\frac1{\Lambda B}
\right).
\tag{36}
\]

The exact Euler atom has the uniform expansion on `Re(s)=1`

\[
H_q(s)=q^{-s}+O(q^{-2}).
\tag{37}
\]

Hence all higher prime powers contribute only

\[
O\!\left(\frac B{Q^2}
+\frac{\Lambda B}{(\Lambda Q)^2}
\right)
=
\frac BQ\,O(Q^{-1}).
\tag{38}
\]

Combining (36)--(38) and `B/Q\asymp d_Q` proves (10).

At `s=1`, the phase term disappears entirely, so the final reciprocal/Euler value is also `o(d_Q)`. But at every cutoff after the local packet and before the remote packet,

\[
\sum_{q\in P_Q}H_q(1)
=\Theta(B/Q)
=\Theta(d_Q),
\tag{39}
\]

which is the selector-scale transient claimed in (7).

## 3. The remote repair remains inside every fixed KV envelope

The local Chebyshev excursion is at most

\[
O(B\log Q)=O(\sqrt Q).
\tag{40}
\]

The remote packet contains `\asymp\Lambda B` primes and therefore contributes at most

\[
O(\Lambda B\log X_1)
=
O\!\left(
\Lambda\sqrt Q\,\frac{\log X_1}{\log Q}
\right).
\tag{41}
\]

At the remote scale `X_1\asymp\Lambda Q`, the ratio of (41) to a fixed KV envelope is

\[
\ll
Q^{-1/2}
\frac{\log X_1}{\log Q}
 e^{bV(X_1)}.
\tag{42}
\]

By (3)--(4), `V(X_1)=o(\log Q)` and `\log X_1` is only polylogarithmic in `Q`. Therefore (42) tends to zero for every fixed `b>0`. The same is true between the shells using (40), and beyond the remote shell the KV envelope is eventually increasing while the perturbation is constant. This proves (11).

Assigning coefficient `+1` to the local primes and `-1` to the remote primes duplicates the former and deletes the latter relative to the ordinary-prime baseline. Thus every multiplicity remains in `{0,1,2}`. No pseudo-primes, continuous weights or negative multiplicities are used.

## Representation audit

The generic mechanism is classical. A finite trigonometric polynomial is Bohr almost periodic, and simultaneous Dirichlet approximation gives an elementary quantitative recurrence for a finite set of frequencies. In the structured case (5), the recurrence cost depends on the rank `r` of the frequency module rather than on the raw number of sampled heights. No novelty is claimed for that harmonic-analysis/Diophantine fact.

The source-specific content is the pullback from an approximate vertical almost-period to the exact ordinary-prime Euler representation at the Robin selector scale: the amplitude loss `\Lambda^{-1}` is compensated by an integer population of remote primes, prime-power harmonics remain negligible, ordinary-prime supply persists in the required tiny intervals, and the whole repair stays inside every fixed KV envelope as long as the logarithmic displacement is `o(\mathcal L_Q)`.

This changes the interpretation of `RE-201`. Its arithmetic DFT grid is the rank-one, exact-period endpoint of a broader phenomenon. Replacing one period by two irrationally related periods raises the alias cost from constant to polynomial in the panel length, but does not eliminate the alias throughout (12). Fully jittering every sample raises the Diophantine dimension, yet a universal cheap recurrence still survives below the `log log Q` sample scale.

## Adversarial self-review

**Does irrationality of two panel spacings defeat the proof?** No. Rational independence removes exact recurrence but is exactly the setting simultaneous approximation addresses. Equation (19) uses no rational relation among the generators.

**Is `\mathcal L_Q` being claimed as a sharp source-fidelity horizon?** No. It is a convenient sufficient scale. The proof needs `V(\Lambda Q)=o(\log Q)` so that the selector-size remote edit remains below every fixed KV envelope. The chosen `\mathcal L_Q` makes that implication transparent. Larger displacements may still be admissible under weaker or more tailored fidelity requirements.

**Can the remote interval contain `\Lambda B` distinct ordinary primes when `\Lambda` is huge?** Yes on the stated displacement range. Equation (29) compares the required population directly with the KV-PNT population of the remote logarithmic bin; the factor `\Lambda` cancels, leaving a `Q^{1/2-o(1)}` margin.

**Could the exact prime powers destroy the simultaneous cancellation at large imaginary height?** No. Their modulus is controlled solely by the real part `Re(s)=1`, giving the extra `Q^{-1}` factor in (38). The only height-sensitive error comes from prime placement inside the bins, and (33) makes it negligible.

**Does this prove that every noncommensurate panel is useless?** No. The structured theorem requires `K^r=o(\mathcal L_Q)`. The arbitrary-panel corollary gives a universal negative result only for `M=o(\log\log Q)`. Above those regimes a carefully designed panel may force all common almost-periods beyond the cheap source-fidelity range. That is now the relevant positive question.

**Does the packet reproduce the complete matched control of `RE-188`--`RE-199` or by itself force an order-one Robin destination change?** No. As in `RE-201`, it proves stable source noncoercivity of the proposed observation family at selector reciprocal scale. It does not simultaneously impose every earlier real-jet matching condition or prove a full Robin countermodel.

**What about several remote shells rather than one translated copy?** They are not ruled out here. Even if a future height design excludes every cheap common translation, a signed combination of several remote shells may still synthesize the sampled vector. The theorem prices the simplest shell-index alias and identifies when incommensurability alone cannot remove it.

## Prior-art audit

A targeted literature search found the expected classical background: Dirichlet/Kronecker simultaneous approximation, Bohr almost periodicity of finite trigonometric sums and Dirichlet-series behavior under vertical translation. Modern treatments of almost periodic functions on vertical strips likewise regard vertical translates as the natural recurrence action. None of that generic recurrence theory is new here.

The simultaneous approximation step is proved directly in (14)--(15), so no new external theorem is load-bearing. The only arithmetic theorem used in the source realization is the Korobov--Vinogradov PNT estimate already anchored for this line. Consequently `SOURCES.md` needs no new durable dependency.

## Literature status

The abstract statement that finitely many frequencies have common approximate periods is classical. The line-specific statement is the quantitative conversion from the **Diophantine rank of a vertical Euler sampling architecture** to a selector-scale ordinary-prime remote alias whose required logarithmic displacement can be compared directly with the KV source-fidelity budget.

The especially useful boundary is (12): using two irrationally related arithmetic panels is not qualitatively different from one commensurate panel until the panel length is large enough that the quadratic Diophantine recurrence cost approaches the KV-safe logarithmic displacement scale.

## Caveats

The result concerns finite vertical samples, not a continuum of imaginary heights. The arbitrary-panel corollary assumes the sampled heights themselves remain `O(M)` so that prime-location quantization errors are negligible; much larger heights require a correspondingly finer prime-placement analysis.

The theorem supplies an upper bound on the distance to an alias, not a matching lower bound for optimally chosen height sets. The thresholds `K^r\sim\mathcal L_Q` and `M\sim\log\log Q` are therefore method/frontier boundaries, not established rigidity transitions.

The finding does not prove RH, Robin's inequality, a zero-free region or a full source-identification theorem.

## Next experiment

Stop testing incommensurability only by adding a second arithmetic grid. There are now two sharper tasks.

First, construct or rule out height sets whose common almost-periods are provably absent throughout `0<L=o(\mathcal L_Q)` at the selector precision needed here. For low-rank spectral modules this becomes a problem in badly approximable vectors; for fully irregular panels the first universal-escape scale exposed by (13) is around `log log Q` samples.

Second, even if single translated-shell aliases are excluded, test whether two or more remote shells with integer prime populations can synthesize the same vertical observation vector while preserving KV fidelity. A positive construction there would show that shell-index rigidity needs more than anti-recurrence; a negative result would finally convert the vertical Fourier capacity of `RE-200` into a genuine source-coercive mechanism.

## Sources

- `RE-200`, *Vertical Euler phase supports linear stable dimension on one prime shell*.
- `RE-201`, *Commensurate vertical Euler frames admit remote-shell aliases at selector debt scale*.
- `RE-015`, for the Korobov--Vinogradov PNT envelope already anchored in `SOURCES.md`.
- T. M. Apostol, *Modular Functions and Dirichlet Series in Number Theory*, 2nd ed., Springer, 1990, Sections 7.4--7.5, as a classical prior-art boundary for Kronecker/simultaneous approximation; the needed pigeonhole estimate is rederived above.
