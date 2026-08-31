# WI-063 — asymptotically lossless spectral sparsification still forces super-polylogarithmic diagonal cost

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical proportion, certify the Yang--Yang one-sided fourth-moment candidate, or resolve the open adversarial review of WI-062. It strengthens the spectral-truncation obstruction of WI-059 in a direction that is independent of WI-062's currently reviewed `h_1(k)` quantifier: for each fixed locally admissible `W`-local pair main, **no arbitrary sparse selection or soft attenuation of Fourier modes can retain asymptotically all of its `L^2` energy while keeping the diagonal conductor-weighted Hilbert cost within any fixed power of `log X`**.

The result is mode-level, not merely a statement about monotone conductor cutoffs. If `B_d(h)` is the exact Fourier energy at reduced conductor `d`, and an arbitrary attenuation retains energy `R_d(h)` with

\[
0\le R_d(h)\le B_d(h),
\]

then asymptotically lossless retention

\[
\frac{\sum_dR_d(h)}{\sum_dB_d(h)}\to1
\]

forces

\[
\boxed{
\frac{\sum_d dR_d(h)}{(\log X)^A}\to\infty
\qquad\text{for every fixed }A>0.
}
\tag{1}
\]

At the Shao--Teräväinen scale `w=(log X)^C`, this closes a natural escape from WI-060--WI-062: one cannot avoid the super-polylogarithmic diagonal cost merely by choosing a clever non-monotone subset of favorable conductors, deleting low-energy modes inside expensive conductors, or replacing a hard cutoff by a smooth spectral taper. Any successful repair must use information that the diagonal conductor-energy ledger discards — genuine cross-conductor arithmetic orthogonality/correlation, a vector-valued dispersion theorem, martingale/Carleson structure, or a direct covariance estimate.

## 1. Exact input from WI-058--WI-059

Use the normalized `W`-local pair main from WI-058,

\[
G_{W,h}=\frac{F_{W,h}}{\mathbb E F_{W,h}},
\qquad
W=\prod_{p\le w}p,
\]

and group its normalized Fourier coefficients by exact reduced conductor:

\[
B_d(h)
:=
\sum_{\operatorname{cond}(\xi)=d}
|\widehat G_{W,h}(\xi)|^2.
\tag{2}
\]

Write

\[
E_h:=\sum_{d\mid W}B_d(h)=\|G_{W,h}\|_2^2.
\tag{3}
\]

On the full active product, WI-059 records the uniform lower energy bound

\[
E_h\gg\log w,
\tag{4}
\]

up to deletion of finitely many source-pinned local primes. More importantly, its fixed-exponent lower-tail theorem says that for every fixed `K>0` there is `c_K>0` such that, uniformly for the locally admissible shifts in the active Yang regime,

\[
\boxed{
\sum_{d>w^K}B_d(h)
\ge c_K E_h
}
\tag{5}
\]

for all sufficiently large `w`. Equivalently, no fixed power `w^K` captures `1-o(1)` of the normalized Fourier energy.

The present finding uses only (3)--(5) plus a one-line weighted truncation inequality. It does not consume the specialization currently under adversarial review in WI-062.

## 2. Allow arbitrary mode-level sparsification

Let each Fourier mode `xi` be multiplied by an arbitrary attenuation `eta_xi` with

\[
|\eta_\xi|\le1.
\]

Hard selection corresponds to `eta_xi` in `{0,1}`, while a soft taper allows intermediate values. Define the retained squared energy at exact conductor `d` by

\[
R_d(h)
:=
\sum_{\operatorname{cond}(\xi)=d}
|\eta_\xi|^2
|\widehat G_{W,h}(\xi)|^2.
\tag{6}
\]

Then automatically

\[
0\le R_d(h)\le B_d(h).
\tag{7}
\]

Set

\[
R_h:=\sum_dR_d(h),
\qquad
H_h:=\sum_d dR_d(h).
\tag{8}
\]

`R_h` is the local-main `L^2` energy retained by the sparsification. `H_h` is exactly the conductor-weighted energy that appears when one performs Cauchy/Parseval separately inside each exact conductor: the physical residue Parseval contributes one factor `d`, while the retained Fourier coefficient square sum contributes `R_d(h)`.

Nothing below assumes that all modes at the same conductor are treated equally. Thus the argument already includes arbitrary within-conductor pruning.

## 3. Exact budget--tail inequality

For every cutoff `D>=1`, split the retained energy at `D`. From (7),

\[
\sum_{d\le D}R_d(h)
\le
\sum_{d\le D}B_d(h).
\tag{9}
\]

For the high-conductor part, the definition of `H_h` gives

\[
\sum_{d>D}R_d(h)
\le
\frac1D
\sum_{d>D}dR_d(h)
\le
\frac{H_h}{D}.
\tag{10}
\]

Therefore

\[
\boxed{
R_h
\le
\sum_{d\le D}B_d(h)
+
\frac{H_h}{D}.
}
\tag{11}
\]

Equivalently, the discarded energy satisfies

\[
\boxed{
E_h-R_h
\ge
\sum_{d>D}B_d(h)
-
\frac{H_h}{D}.
}
\tag{12}
\]

This is the entire optimization step. It shows directly why a clever non-monotone selection cannot beat a conductor threshold at the information-interface level: every unit of retained squared Fourier energy at conductor `d` costs `d` units in `H_h`, regardless of which individual mode carries it.

No novelty is claimed for (11)--(12); they are an elementary weighted Markov/knapsack inequality. The source-specific consequence comes from combining them with the exact `W`-local conductor law of WI-058--WI-059.

## 4. Lossless retention forces cost beyond every fixed log power

Use the source scale

\[
w=(\log X)^C
\tag{13}
\]

with fixed `C>0`. Suppose the attenuation is asymptotically lossless:

\[
\frac{R_h}{E_h}\to1.
\tag{14}
\]

Fix any `A>0`. Assume for contradiction that

\[
\frac{H_h}{(\log X)^A}
\not\to\infty.
\tag{15}
\]

Then there are a constant `M` and an unbounded subsequence on which

\[
H_h\le M(\log X)^A.
\tag{16}
\]

Choose

\[
D=(\log X)^{A+2}
=w^{K_A},
\qquad
K_A:=\frac{A+2}{C}.
\tag{17}
\]

`K_A` is a **fixed** exponent, so WI-059 applies. Equations (5), (12), and (16) give on that subsequence

\[
\begin{aligned}
E_h-R_h
&\ge
c_{K_A}E_h
-
\frac{M(\log X)^A}{(\log X)^{A+2}}\\
&=
 c_{K_A}E_h
-
\frac{M}{(\log X)^2}.
\end{aligned}
\tag{18}
\]

Divide by `E_h`. By (4), `E_h\gg\log w\to\infty`, so the final term is `o(1)`. Hence

\[
\liminf
\frac{E_h-R_h}{E_h}
\ge c_{K_A}>0,
\tag{19}
\]

contradicting (14). Therefore (15) is impossible, proving (1).

The argument is uniform for every locally admissible shift family for which WI-059's active-prime lower-tail statement applies. In particular, allowing the sparsification itself to depend on `h` does not change the conclusion: (11)--(19) are pointwise in `h`.

## 5. Absolute `L^2` accuracy is covered automatically

Some splice formulations demand the stronger condition

\[
E_h-R_h=o(1)
\tag{20}
\]

rather than merely relative capture. Since (4) gives `E_h\to\infty`, (20) implies (14). Therefore the same super-polylogarithmic cost barrier applies a fortiori to every attenuation whose discarded deterministic local-main `L^2` energy is absolutely `o(1)`.

This matters because WI-058--WI-059 use exactly such an absolute-tail gate when trying to make the unretained `W`-local main harmless by a norm estimate. The present result says that changing the **shape** of the retained spectral set does not rescue that strategy.

## 6. Consequence for the Mikawa repair architecture

WI-061 identifies Mikawa's conditioned prime-pair theorem as the correct single-conductor arithmetic input. If an attenuated exact-conductor contribution is written schematically as

\[
C_d^{\eta}(k)
=
\sum_{\operatorname{cond}(\xi)=d}
\eta_\xi
\widehat G_{h_1(k)}(\xi)
\,T_{d,\xi}(h_2(k)),
\tag{21}
\]

then Cauchy in the Fourier modes followed by residue Parseval has a first factor precisely of the form `R_d(h_1(k))`, and the residue transform contributes the physical conductor factor `d`. Thus any repair that **scalarizes each conductor to a diagonal norm before assembling conductors** inherits a coefficient of the form

\[
dR_d.
\tag{22}
\]

The current WI-062 review concerns how the varying `h_1(k)` must be quantified when that per-shift coefficient is extracted across the booked `k`-family. The present barrier deliberately does not assume an answer to that review. It says something prior and pointwise: even at one fixed admissible `h`, there is no asymptotically lossless mode selection for which the diagonal coefficient sum `sum_d dR_d(h)` stays polylogarithmic.

Consequently the following three apparent escapes are closed inside the diagonal architecture:

1. keep only a non-monotone sparse set of especially favorable conductors;
2. keep only a sparse set of modes inside each expensive conductor;
3. replace the hard cutoff of WI-059 by any soft attenuation chosen from the exact Fourier amplitudes.

All three still satisfy (7), hence all three obey (1) if they retain `1-o(1)` of the local-main energy.

What remains open is exactly what WI-060--WI-062 were pointing toward: an estimate that **does not reduce the conductor family to diagonal norms**. Cross-conductor cancellation, arithmetic projection relations, a vector-valued Mikawa/dispersion theorem, a large-sieve inequality adapted to the actual pair-error family, or a direct source-normalized covariance theorem could use information absent from `H_h` and are not touched by this no-go.

## 7. Stress tests and scope

Several stronger readings are intentionally excluded.

- Equation (1) does **not** say that the actual Yang conductor contributions are aligned or that their signed sum is large. It only says that diagonal energy bookkeeping cannot make the coefficient budget polylogarithmic while remaining spectrally lossless.
- The result does **not** rule out a lossy spectral projection whose discarded modes are controlled by some arithmetic cancellation stronger than their own `L^2` norm. Its hypothesis is precisely that the retained spectrum itself captures `1-o(1)` of the deterministic local-main energy.
- It does **not** rule out a cross-conductor theorem whose hypotheses involve the actual residue/character geometry before per-conductor scalarization. Such a theorem would add information absent from (7)--(8).
- It does **not** depend on ordering conductors by size in the chosen sparsification. The threshold `D` appears only as a comparison device in (11)--(12); the retained set may be arbitrary.
- Finitely many pinned local primes do not affect the conclusion because WI-059's fixed-`K` lower tail and (4) are stable under deleting them.

## 8. Prior-art and novelty audit

The underlying optimization inequality (11)--(12), hard/soft thresholding, and the observation that a weighted budget bounds mass above a cost threshold are elementary and are not claimed as new. The arithmetic input — the exact product law for `W`-local Fourier-conductor energy and the fixed-exponent positive tail — is already persisted in WI-058--WI-059.

A bounded targeted public search around `W`-trick Fourier conductor energy, exact-conductor truncation, Ramanujan/Fourier conductor decompositions, and spectral sparsification did not locate a source stating this particular source-normalized consequence for the Shao--Teräväinen pair main. That absence is **not** used as evidence of priority. The durable Mathia contribution claimed here is only the exact deduction that WI-059's positive fixed-exponent tail defeats *every* asymptotically lossless diagonal mode-selection/taper scheme, not just raw initial conductor cutoffs.

## 9. Decisive falsification / narrowing gate

Narrow or retire this finding if any of the following is shown.

1. WI-059's fixed-exponent positive Fourier-energy tail (5) fails in the actual active shift family used by the Yang splice after all source-pinned primes are accounted for.
2. A proposed mode selection retains `1-o(1)` of the deterministic local-main `L^2` energy while its exact conductor-weighted energy `sum_d dR_d` is only `(log X)^{O(1)}`; by (11)--(19), such an example would directly falsify one of the stated inputs.
3. The intended arithmetic assembly can be written without a diagonal coefficient comparable to `dR_d` because a proved cross-conductor identity/orthogonality is used **before** scalarization. This would not falsify the theorem (1), but it would narrow its relevance by escaping its information interface.

Until such an escape is supplied, conductor selection itself is no longer a credible way around the WI-060--WI-062 bottleneck. The next evidence-changing target remains genuinely collective arithmetic structure across conductors rather than a more elaborate spectral cutoff.
