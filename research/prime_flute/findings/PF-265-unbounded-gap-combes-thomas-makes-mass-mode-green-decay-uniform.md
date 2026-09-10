# PF-265 — unbounded-gap Combes–Thomas makes mass-mode Green decay uniform

**Status:** `LITERATURE+DERIVED + UNIFORM-MASS-GREEN-DECAY + ADAPTIVE-JACOBI-METRIC + FINITE-SEAM-ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-261-finite-seam-crossover-is-a-bounded-positive-mixture-of-massive-axis-resolvents|PF-261]] turns the exact finite-seam crossover into an odd-mass sum of Green matrices `(L+a_k^2)^{-1}`. [[research/prime_flute/findings/PF-262-massive-jacobi-resolvents-have-exact-double-root-indicial-law|PF-262]]--[[research/prime_flute/findings/PF-264-fixed-mass-green-kernel-has-universal-two-index-leading-law|PF-264]] then identify the sharp **fixed-mass** asymptotic

\[
G_{ij}^{(\varepsilon)}(a)
\sim \frac{1}{2\mu\sqrt{ij}}
\left(\frac{i}{j}\right)^\mu,
\qquad
\mu=\sqrt{1+a^2},
\qquad i\le j\to\infty,
\tag{1}
\]

inside each parity block. The remaining caveat was that the asymptotic errors in (1) are only pointwise in `a`, so the mass ladder cannot be summed from PF-264 alone.

A classical unbounded-Jacobi Combes--Thomas theorem gives a genuinely uniform part of the missing statement. Specialized to the exact PF parity blocks, it yields an all-mass/all-mode Green estimate with an explicit constant because the spectral parameter `-a^2` lies below the **whole** spectrum, not merely below the essential spectrum. In particular there are constants `C_p>=1` and `c_p>0`, depending only on the two fixed parity recurrences, such that for every `a>=0`, `i<j`, and `\varepsilon\in\{0,1\}`,

\[
\boxed{
|G_{ij}^{(\varepsilon)}(a)|
\le \frac{4}{\mu^2}
\exp\!\left[-\sum_{m=i}^{j-1}
\min\!\left(1,\frac{c_p\mu}{m+1}\right)\right].
}
\tag{2}
\]

Hence, whenever `c_p\mu\le i+1`,

\[
\boxed{
|G_{ij}^{(\varepsilon)}(a)|
\le \frac{4}{\mu^2}
\left(\frac{i+1}{j+1}\right)^{c_p\mu}.
}
\tag{3}
\]

There is also a complementary large-mass estimate. With `A_p=\sqrt{2C_p}`, if `\mu\ge A_p(j+1)` and `d=j-i`, then

\[
\boxed{
|G_{ij}^{(\varepsilon)}(a)|
\le \frac{4}{\mu^2}
\left(\frac{A_p(j+1)}{\mu}\right)^d.
}
\tag{4}
\]

Thus on the accepted clue's separated cone `j\ge2i+2`, where `d>=2`, the sufficiently large odd-mass tail in PF-261 is absolutely summable for every fixed pair of mode indices. The mass dependence of the **decay exponent** is therefore not an uncontrolled connection-coefficient problem.

The result does **not** close the finite-seam `R>1` target. The uniform Combes--Thomas prefactor is `O(\mu^{-2})`, whereas PF-264's sharp moving-source law carries the additional mode amplitude `1/\sqrt{ij}`. After PF-261's outer endpoint weights that difference is exactly material at the one-dimensional trace threshold. The surviving problem has sharpened from “make the whole fixed-mass asymptotic uniform” to **recover enough of PF-264's sharp mode amplitude uniformly in the coupled mass/mode regime and only then sum the odd ladder**.

## 1. Exact below-spectrum setup

PF-238 identifies

\[
L=U(1-\partial_\tau^2)U^*
\tag{5}
\]

on `L^2((0,\pi),d\theta)`, with `\tau=\log\tan(\theta/2)`. Reflection `\theta\mapsto\pi-\theta` corresponds to `\tau\mapsto-\tau`; the even and odd Gegenbauer sectors of PF-247 are therefore the even and odd restrictions of `1-\partial_\tau^2`. Consequently each self-adjoint parity block satisfies

\[
\boxed{
\sigma(L_\varepsilon)=[1,\infty),
\qquad L_\varepsilon\ge I.
}
\tag{6}
\]

This self-adjointness is inherited from the differential realization. It is important not to invoke the sufficient Carleman criterion for the parity Jacobi coefficients: PF-262 has `|p_m|\asymp m^2`, so `\sum_m|p_m|^{-1}` converges and that criterion is unavailable.

Write the parity recurrence as

\[
p_{m-1}u_{m-1}+q_mu_m+p_mu_{m+1}=0.
\tag{7}
\]

PF-262 proves, for each parity,

\[
p_m=-m^2-c_\varepsilon m-d_\varepsilon+O(m^{-1}).
\tag{8}
\]

Hence one may fix a single `C_p>=1` so that

\[
|p_m^{(\varepsilon)}|\le C_p(m+1)^2
\tag{9}
\]

for both parities and every `m>=0`.

## 2. The unbounded-gap Green theorem specializes with an explicit uniform constant

Janas, Naboko, and Silva, *Green matrix estimates of block Jacobi matrices I: Unbounded gap in the essential spectrum*, Integral Equations and Operator Theory 90 (2018), Paper 49, DOI `10.1007/s00020-018-2476-0`, arXiv:1801.01924v2, Theorem 3.1, introduce

\[
\psi(x)=x^2e^x,
\qquad
\phi_\delta(x)=\frac1{\sqrt{\max(\delta,x)}}
\tag{10}
\]

and prove a Combes--Thomas estimate for a self-adjoint semibounded block Jacobi operator below a lower essential-spectral edge `b`. In scalar form, for `\Re\lambda<b`,

\[
|G_{ij}(\lambda)|
\le C\exp\!\left[-\gamma(\lambda)
\sum_{m=i}^{j-1}\phi_\delta(|p_m|)\right],
\tag{11}
\]

where

\[
\gamma(\lambda)
=\sqrt\delta\,
\psi^{-1}\!\left(\frac{(b-\Re\lambda)(1-\epsilon)}{\delta}\right).
\tag{12}
\]

The theorem allows unbounded Jacobi matrices: each scalar off-diagonal entry is a bounded block, while the sequence of block norms may grow.

For the PF block take

\[
b=1,
\qquad \lambda=-a^2,
\qquad b-\lambda=1+a^2=\mu^2,
\qquad \epsilon=\frac12.
\tag{13}
\]

Because (6) has **no spectrum at all below `b`**, the compact correction

\[
K=(L_\varepsilon-b)E(-\infty,b)
\tag{14}
\]

in the proof of Theorem 3.1 vanishes identically. Equation (3.16) of that proof therefore gives the explicit constant

\[
C=\frac{2}{\epsilon(b-\lambda)}=\frac4{\mu^2}
\tag{15}
\]

with no hidden dependence on `a`, `i`, `j`, or `\delta`. Thus for every `\delta>0`,

\[
\boxed{
|G_{ij}^{(\varepsilon)}(a)|
\le \frac4{\mu^2}
\exp\!\left[-\sqrt\delta\,
\psi^{-1}\!\left(\frac{\mu^2}{2\delta}\right)
\sum_{m=i}^{j-1}\phi_\delta(|p_m^{(\varepsilon)}|)
\right].
}
\tag{16}
\]

This is already a parameter-uniform theorem, before any asymptotic reduction of the PF coefficients.

## 3. An adaptive choice gives a uniform ratio metric

Choose

\[
\delta=\frac{\mu^2}{2e}.
\tag{17}
\]

Since `\psi(1)=e`, equation (16) has

\[
\gamma=\frac{\mu}{\sqrt{2e}}.
\tag{18}
\]

Using (9),

\[
\phi_\delta(|p_m|)
\ge
\frac1{\sqrt{\max(\delta,C_p(m+1)^2)}}.
\tag{19}
\]

Therefore, with

\[
c_p:=\frac1{\sqrt{2eC_p}},
\tag{20}
\]

one has the pointwise metric lower bound

\[
\gamma\phi_\delta(|p_m|)
\ge
\min\!\left(1,\frac{c_p\mu}{m+1}\right).
\tag{21}
\]

Substitution into (16) proves (2). If `c_p\mu\le i+1`, no term in (21) saturates, and

\[
\sum_{m=i}^{j-1}\frac1{m+1}
\ge\log\frac{j+1}{i+1},
\tag{22}
\]

which proves (3).

The exponent in (3) is deliberately not advertised as sharp. Corollary 3.1 of the same paper shows that for each fixed spectral parameter the coefficient in front of `\sum|p_m|^{-1/2}` can be taken arbitrarily close to `\sqrt{b-\lambda}=\mu`; together with `|p_m|\sim m^2`, that reproduces the fixed-mass ratio exponent from PF-264 up to an arbitrarily small loss. But the constant in that corollary depends on the spectral parameter. Equation (2), by contrast, keeps an explicit all-mass constant.

## 4. A second adaptive choice controls the genuinely large-mass ladder

For fixed `i<j`, choose instead

\[
\delta=C_p(j+1)^2.
\tag{23}
\]

Then (9) implies `|p_m|<\delta` for every `i\le m\le j-1`, so

\[
\sum_{m=i}^{j-1}\phi_\delta(|p_m|)
=\frac{d}{\sqrt{C_p}(j+1)},
\qquad d=j-i.
\tag{24}
\]

Put

\[
x=\frac{\mu^2}{2C_p(j+1)^2}.
\tag{25}
\]

Equation (16) becomes

\[
|G_{ij}^{(\varepsilon)}(a)|
\le\frac4{\mu^2}
\exp[-d\,\psi^{-1}(x)].
\tag{26}
\]

If `x>=1`, equivalently `\mu\ge A_p(j+1)` with `A_p=\sqrt{2C_p}`, then for `t=\psi^{-1}(x)` one has `x=t^2e^t` and the elementary inequality `2\log t\le t` for `t>0`. Hence

\[
t\ge\frac12\log x,
\tag{27}
\]

and (4) follows.

For PF-261's odd masses `a_k=(2k+1)\pi/(2rs)`, one has `\mu_k\asymp a_k` in the large-mass tail. Since `a_k^2/\mu_k^2<=1`, equation (4) implies

\[
a_k^2|G_{ij}^{(\varepsilon)}(a_k)|
=O_{i,j,s}(a_k^{-d}).
\tag{28}
\]

Thus the sufficiently large-mass part of the exact PF-261 series converges absolutely whenever `d>1`; in particular this holds throughout `j\ge2i+2`. This removes a possible failure mode in which arbitrarily large masses could defeat the fixed-mass recession by uncontrolled connection coefficients.

## 5. Why this still stops at the critical weighted threshold

The estimate that PF-261 ultimately needs is not merely convergence of the mass sum. It needs enough **mode amplitude** after the outer factor

\[
\frac1{\sqrt{\kappa_i\kappa_j}}
\tag{29}
\]

to retain strict separated smoothing `R>1` and then survive the combined Robin transform from PF-257/PF-243.

Here the distinction between (2) and PF-264 is load-bearing. At fixed mass and `i\asymp j`, PF-264 has

\[
|G_{ij}(a)|\asymp
\frac1{\mu\sqrt{ij}}
\left(\frac{i}{j}\right)^\mu,
\tag{30}
\]

whereas (2) controls only

\[
|G_{ij}(a)|
\lesssim\mu^{-2}
\left(\frac{i}{j}\right)^{c_p\mu}
\tag{31}
\]

in its unsaturated regime. The missing `1/\sqrt{ij}` is not cosmetic: after (29), (31) naturally lands at a one-dimensional **critical** `j^{-1}`-type amplitude on a fixed separated ratio, while (30) supplies the extra mode power that can cross into strict `R>1` territory after the mass sum.

Therefore the uniformity question exposed by PF-264 has split cleanly into two pieces:

1. **decay metric / mass recession:** now controlled uniformly by (2)--(4);
2. **sharp Green amplitude:** still open uniformly when `a`, `i`, and `j` move together.

A proof should not spend more effort rebuilding a mass-uniform exponential/rational decay mechanism that the general Jacobi theorem already supplies. It should attack the amplitude normalization, or show that it genuinely blows up in a coupled transition regime.

## 6. Prior art and novelty audit

The principal imported result is classical and is not claimed as new:

- J. Janas, S. Naboko, L. O. Silva, *Green matrix estimates of block Jacobi matrices I: Unbounded gap in the essential spectrum*, Integral Equations and Operator Theory **90** (2018), Paper 49, DOI `10.1007/s00020-018-2476-0`, arXiv:1801.01924v2. Theorem 3.1 gives (11)--(12); its proof gives the explicit constant used in (15), and Corollary 3.1 gives the sharper fixed-spectral-parameter coefficient.
- J. Janas, S. Naboko, G. Stolz, *Decay bounds on eigenfunctions and the singular spectrum of unbounded Jacobi matrices*, International Mathematics Research Notices **2009** (4), 736--764, DOI `10.1093/imrn/rnn144`, is the earlier scalar semibounded theory on which the 2018 result builds.
- S. Naboko, S. Simonov, *Estimates of Green matrix entries of selfadjoint unbounded block Jacobi matrices*, St. Petersburg Mathematical Journal **35** (2024), 185--199, DOI `10.1090/spmj/1800`, is later related Green-matrix prior art for broader unbounded block-Jacobi classes.

The 2018 paper itself explicitly presents its estimates as a refinement/generalization of Combes--Thomas decay whose metric depends inversely on growth of the off-diagonal Jacobi entries. No novelty is claimed for that theorem, the `|p_m|\asymp m^2` harmonic metric, or the existence of sharp scalar bounds below the spectrum.

The project-specific content here is the exact specialization to PF-247/PF-262's parity realization, the observation that PF-238 gives `L_\varepsilon>=I` so the paper's compact below-edge correction vanishes and yields the explicit all-mass prefactor `4/\mu^2`, the two adaptive choices of `\delta`, and the resulting separation of the finite-seam obstruction into a **known uniform decay metric** versus an **unknown sharp mode amplitude**. A targeted literature audit found general Jacobi Green-decay theorems, but no theorem identified in this pass that supplies PF-264's `1/(\mu\sqrt{ij})` amplitude uniformly over the coupled mass/mode family required by PF-261.

## 7. Boundaries and adversarial checks

1. **Self-adjointness does not come from Carleman.** The parity Jacobi off-diagonals grow quadratically, so the sufficient Carleman sum converges. The required self-adjoint operator is instead the parity restriction of PF-238's explicit self-adjoint differential operator.
2. **The spectral gap is exact.** The choice `b=1` is justified by the unitary complete-axis model, not by the asymptotic Jacobi coefficients. There is no hidden discrete spectrum below `1`, hence `K=0` in the imported proof.
3. **The all-mass constant is explicit only for the Theorem 3.1 form.** Corollary 3.1 recovers an exponent arbitrarily close to the sharp fixed-mass value but its constant may depend on `a`; it cannot simply replace (2) inside the odd-mass sum.
4. **Coefficient signs are irrelevant to this estimate.** The imported bound uses the norm of the off-diagonal block, hence `|p_m|`; PF's negative Jacobi gauge causes no sign assumption.
5. **Large-mass absolute convergence is not a uniform seam estimate.** Equation (28) is for a fixed mode pair before the weighted operator norm. It does not justify an interchange of all limits or prove the required `R>1` operator bound.
6. **No sharp amplitude is proved.** Nothing here upgrades `4/\mu^2` to PF-264's `1/(2\mu\sqrt{ij})` uniformly. That is now the main fixed-axis analytic gate.
7. **No actual-corridor/Robin conclusion.** PF-256's variable `K_a` basis, hypercycle transport, the combined PF-257 Robin transform, PF-243 Poisson factorization, finite-pant completion, global weak-trace reassembly, scattering/determinants, zeta zeros, and RH all remain outside this finding.

The finding would fail if the parity restriction were not the self-adjoint `L_\varepsilon>=I` realization used above, if PF-262's off-diagonal coefficients did not obey a uniform quadratic upper bound, or if Theorem 3.1's proof retained a nonzero below-edge compact correction in this exact below-spectrum situation. The persisted PF identities and the cited theorem exclude those cases.

## Decisive next test

Attack the **uniform amplitude**, not the decay exponent. A natural sharp interpolation target for the diagonal is

\[
\boxed{
G_{ii}^{(\varepsilon)}(a)
\lesssim \frac{1}{\mu(i+\mu)}
}
\tag{32}
\]

uniformly in `a` and large `i`: it matches PF-264's fixed-mass `1/(2\mu i)` scale when `i\gg\mu` and the trivial large-mass resolvent scale `O(\mu^{-2})` when `\mu\gg i`. Prove such an estimate, or another estimate with the same load-bearing mode gain, and determine whether it can be combined with the uniform off-diagonal metric (2) to recover

\[
|G_{ij}^{(\varepsilon)}(a)|
\lesssim
\frac{1}{\mu\sqrt{ij}}
\left(\frac{i+1}{j+1}\right)^{c\mu}
\tag{33}
\]

on a separated cone with constants uniform in the coupled mass/mode regimes. Then sum PF-261's **actual odd ladder before taking the weighted norm** and propagate only the surviving strict `R>1` margin through the combined Robin map. If (32) or an equivalent amplitude normalization fails, identify the transition regime and test whether that failure truly destroys every strict `R>1` finite-seam bound.