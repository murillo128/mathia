# AF-237 — linear Li jet truncation creates a spurious trivial-zero root rate

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `RH-SUFFICIENT-QUOTIENT`, `TARGET-METRIC`, `CANCELLATION-COHERENCE`, `NO-NOVELTY-CLAIM`

## Claim

AF-236 proves that every sublinear initial jet of the classical `eta`-coefficient reconstruction is invisible in the AF-235 Li root-rate quotient. The first scale not excluded there is linear depth. Linear depth, however, is not automatically faithful.

Keep the notation

\[
g'(w)=\frac1w+\frac{\zeta'}{\zeta}(1+w)
      =-\sum_{j\ge0}\eta_j w^j,
\qquad
Z_n^{\le K}=-\sum_{k=1}^{K_n}\binom nk\eta_{k-1}.
\tag{1}
\]

Fix

\[
0<\alpha<\frac14,
\qquad
K_n=\lfloor \alpha n\rfloor.
\tag{2}
\]

Then the nearest singularity of `g'` after the cancelled pole at `w=0` is the simple pole at `w=-3`, coming from the first trivial zeta zero `s=-2`. It forces the exact exponential rate

\[
\boxed{
\lim_{n\to\infty}
\left|Z_n^{\le \lfloor\alpha n\rfloor}\right|^{1/n}
=
\frac{\exp(H(\alpha))}{3^\alpha}
>1,
}
\tag{3}
\]

where

\[
H(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)
\tag{4}
\]

is binary entropy in natural units.

Thus every fixed positive jet fraction below `1/4` produces an **exponentially visible false signal regardless of RH**. If the explicit completion term from AF-234 is restored,

\[
\widetilde\lambda_n^{(\alpha)}
:=A_n+Z_n^{\le\lfloor\alpha n\rfloor},
\tag{5}
\]

then `A_n=O(n log n)` is subexponential, so

\[
\lim_{n\to\infty}
|\widetilde\lambda_n^{(\alpha)}|^{1/n}
=
\frac{\exp(H(\alpha))}{3^\alpha}>1.
\tag{6}
\]

But AF-235 identifies root rate at most `1` as the RH-sufficient class of the **full** Li sequence. Hence a naively truncated linear jet with `0<alpha<1/4` lies outside that class unconditionally. The exponential growth is not evidence for an off-critical zero: it is an artifact of interrupting the binomial cancellation of the known trivial zero.

This sharpens the AF-236 depth boundary. The issue is not merely that the source must be deep enough. A source approximation must be **cancellation-coherent** with singularities that the exact global transform cancels. Positive linear depth can be worse than sublinear depth: the former can manufacture a decisive-looking root-rate signal that the latter cannot see at all.

## Derivation

### 1. Isolate the first trivial-zero pole

The trivial zeros of `zeta(s)` occur at the negative even integers. The first is `s=-2`, corresponding to `w=s-1=-3`; the next is `s=-4`, corresponding to `w=-5`. The first nontrivial zero occurs at height about `14.1347`, so there is no other zeta zero in the disk `|w|<5` after the `w=-3` pole is removed.

Therefore

\[
h(w):=g'(w)-\frac1{w+3}
\tag{7}
\]

is analytic on `|w|<5`. Write

\[
h(w)=\sum_{j\ge0}c_jw^j.
\tag{8}
\]

Since

\[
\frac1{w+3}
=\sum_{j\ge0}\frac{(-1)^j}{3^{j+1}}w^j,
\tag{9}
\]

comparison with `(1)` gives

\[
\eta_j
=\frac{(-1)^{j+1}}{3^{j+1}}-c_j.
\tag{10}
\]

Hence

\[
Z_n^{\le K}=P_{n,K}+E_{n,K},
\tag{11}
\]

with

\[
P_{n,K}:=-\sum_{k=1}^{K}\binom nk\frac{(-1)^k}{3^k},
\qquad
E_{n,K}:=\sum_{k=1}^{K}\binom nk c_{k-1}.
\tag{12}
\]

The first term is the contribution forced solely by the known trivial zero `s=-2`; the second contains everything analytic beyond radius `3`.

### 2. The incomplete trivial-zero cancellation has an endpoint large-deviation rate

Set

\[
a_{n,k}=\binom nk3^{-k}.
\tag{13}
\]

For `k<=K_n=floor(alpha n)`,

\[
\frac{a_{n,k-1}}{a_{n,k}}
=\frac{3k}{n-k+1}
\le
\frac{3K_n}{n-K_n+1}
\longrightarrow
\frac{3\alpha}{1-\alpha}<1,
\tag{14}
\]

because `alpha<1/4`. Thus the magnitudes in the alternating sum increase up to the retained endpoint. Reversing the sum gives an alternating series with decreasing magnitudes, so

\[
a_{n,K_n}-a_{n,K_n-1}
\le
\left|\sum_{k=0}^{K_n}(-1)^k a_{n,k}\right|
\le
a_{n,K_n}.
\tag{15}
\]

The ratio in `(14)` stays bounded away from `1`, so `(15)` and Stirling's formula imply

\[
\lim_{n\to\infty}
\left|\sum_{k=0}^{K_n}(-1)^k a_{n,k}\right|^{1/n}
=
\lim_{n\to\infty}a_{n,K_n}^{1/n}
=
\frac{\exp(H(\alpha))}{3^\alpha}.
\tag{16}
\]

Since `P_{n,K}=1-sum_{k=0}^K(-1)^k a_{n,k}`, and the right-hand side of `(16)` is greater than `1` for `0<alpha<1/4`, the same root rate holds for `P_{n,K_n}`.

The full contribution of this pole would instead be

\[
-\sum_{k=1}^{n}\binom nk\frac{(-1)^k}{3^k}
=1-\left(\frac23\right)^n,
\tag{17}
\]

which is bounded. Thus `(16)` is literally the exponential cost of stopping the cancellation early: exponentially large intermediate binomial terms cancel in the full transform but survive in the initial linear truncation.

### 3. The analytic remainder cannot cancel the first-pole rate

Fix `alpha<1/4`. Choose a radius `R` such that

\[
3<R<\min\left\{5,\frac1\alpha-1\right\}.
\tag{18}
\]

This is possible exactly because `alpha<1/4`. Cauchy's estimate applied to `(8)` gives a constant `C_R` with

\[
|c_j|\le C_R R^{-j}.
\tag{19}
\]

For `k<=K_n`, the terms `binom(n,k)R^{-k}` are increasing for large `n`, because `alpha<1/(R+1)`. Hence, up to a polynomial factor,

\[
|E_{n,K_n}|
\le C_R R K_n\binom n{K_n}R^{-K_n}.
\tag{20}
\]

Therefore

\[
\limsup_{n\to\infty}|E_{n,K_n}|^{1/n}
\le
\frac{\exp(H(\alpha))}{R^\alpha}
<
\frac{\exp(H(\alpha))}{3^\alpha}.
\tag{21}
\]

So the remainder is exponentially smaller than the `w=-3` contribution and cannot cancel it. Equations `(16)` and `(21)` prove `(3)`.

Finally, for `0<alpha<1/4`, both terms in

\[
H(\alpha)-\alpha\log3
=-\alpha\log(3\alpha)-(1-\alpha)\log(1-\alpha)
\tag{22}
\]

are positive, so the rate in `(3)` is strictly greater than `1`.

## Why this is an Arithmetic Fidelity result

AF-235 showed that RH survives a huge destination compression: all subexponential additive information in the Li sequence can be discarded. AF-236 then showed that every `o(n)` local zeta jet is too shallow to reach that quotient. AF-237 exposes the complementary failure mode at the first larger scale.

The exact Li transform is not a monotone accumulation of useful source information. Its global cancellation pattern is itself part of the information that must survive. Keeping more coefficients while breaking that pattern can create an exponentially wrong destination class. In fidelity language, **source depth and source coherence are independent resources**.

This is a concrete warning against judging an RH-facing compression by retained cardinality alone. A retained fraction may be linear and yet fail catastrophically because it cuts across a cancellation orbit generated by a known, irrelevant singularity.

## Matched controls and boundaries

**Sublinear control.** AF-236 gives `Z^{<=K} in S` for every `K_n=o(n)`. Such truncations are invisible rather than falsely exponential. AF-237 therefore identifies a genuine change of failure mode between vanishing-fraction and fixed-fraction depth.

**Full-depth control.** The isolated trivial-zero pole contributes only `1-(2/3)^n` when all `n` binomial terms are retained. Its exponential artifact is entirely a truncation effect.

**Quarter-depth boundary.** The theorem proves `(3)` only for `0<alpha<1/4`. At `alpha=1/4` the magnitudes `binom(n,k)3^{-k}` reach their saddle, and beyond it endpoint monotonicity no longer supplies `(15)`. This is a proof boundary, not a claim that the artifact disappears at one quarter.

**Known-trivial-zero origin.** No RH assumption enters. The dominant pole is the classical zero `s=-2`; nontrivial zeros lie outside the analytic disk used to bound the remainder. The theorem therefore cannot be interpreted as partial evidence for or against RH.

**Coordinate dependence.** The obstruction belongs to the canonical local-`eta` binomial reconstruction. A different representation may package or cancel the trivial-zero contribution before truncation. Such a representation would be a legitimate escape only if its own source-to-target sufficiency and information cost are established independently.

**Exact coefficients.** Numerical precision is not responsible for the effect. Even exact knowledge of every retained `eta_j` produces the exponential artifact.

## Prior art and novelty assessment

The Li/Keiper coefficient representation and the `eta_j` Laurent coefficients are classical. Mark W. Coffey's work on the Li criterion develops the exact alternating binomial component in `(1)` and its relation to the local logarithmic derivative of zeta; see **“Toward Verification of the Riemann Hypothesis: Application of the Li Criterion,”** *Mathematical Physics, Analysis and Geometry* 8 (2005), 211–255, DOI `10.1007/s11040-005-7584-9`, and **“The Stieltjes constants, their relation to the eta_j coefficients, and representation of the Hurwitz zeta function,”** arXiv:`0706.0343` (2007).

The NIST DLMF §25.10 is an authoritative reference for the trivial zeros `zeta(-2m)=0`. The LMFDB Riemann-zeta zero dataset records the first nontrivial zero at height about `14.1347`; its dataset documentation states that the zero list was computed with rigorous Turing-method completeness checks. These classical facts justify the analytic separation between the `w=-3` pole and the remainder in `(7)`.

Incomplete and alternating finite binomial sums are a classical topic, and the endpoint estimate `(15)` is elementary. A targeted search across Li/`eta` literature, incomplete-binomial-sum literature, and singularity-asymptotic formulations did not locate the specific fixed-fraction truncation statement `(3)` or its interpretation as a false Li root-rate signal. No literature novelty claim is made. The durable contribution here is the exact derived obstruction and its fidelity interpretation: **a known trivial zero forces exponentially wrong root-rate behavior for every initial linear jet fraction below one quarter, even though its fully cancelled Li contribution is bounded.**

## Evidence boundary

Equation `(3)` is an unconditional asymptotic theorem for the declared truncation `K_n=floor(alpha n)` with `0<alpha<1/4`. Its proof uses only the classical local `eta` representation, the location of the first two trivial zeros and absence of nontrivial zeros in the small disk, Cauchy estimates, elementary alternating-sum bounds, and Stirling asymptotics.

It does not identify the minimum faithful linear depth, does not prove that any fixed fraction is sufficient, and does not classify truncations at or above `alpha=1/4`. It also does not price the precision needed for deep `eta_j`, produce a prime-side estimate, or supply an RH proof.

## Consequences for the research frontier

The next Li-facing source bridge must now pass a stronger gate than AF-236 imposed. It is not enough to reach linear coefficient depth. The representation must also preserve or analytically remove the cancellation associated with destination-irrelevant singularities such as the trivial zeros before the root-rate quotient is read.

A promising continuation is therefore to classify **cancellation-coherent truncations or preconditionings** of the local zeta germ: for example, remove known completion/trivial-zero factors before truncation, then determine whether the remaining source depth needed to control the AF-235 quotient genuinely falls. The decisive test is whether such preprocessing reduces source access without importing the nontrivial zero divisor or merely repackages the full Li transform.