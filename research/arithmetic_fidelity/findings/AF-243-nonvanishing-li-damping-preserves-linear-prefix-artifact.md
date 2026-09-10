# AF-243 — nonvanishing Li damping preserves a linear-prefix artifact window

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `RH-SUFFICIENT-QUOTIENT`, `CANCELLATION-COHERENCE`, `INFORMATION-PRICE`, `SCALE-DEPENDENT-FILTER`, `NO-NOVELTY-CLAIM`

## Claim

AF-239--AF-242 show that a full binomial Li orbit can be damped in a cancellation-coherent way, and that schedules `t_n -> 1` can preserve the ordinary RH root-rate discriminator while suppressing every fixed critical-line zero. That does **not** make a shallow initial segment of the same source orbit faithful.

Write

\[
Q(w):=\frac{\xi'}{\xi}(1+w)=\sum_{j\ge0}b_jw^j
\tag{1}
\]

and let

\[
\rho_1=\frac12+i\gamma_1,
\qquad
\gamma_1\approx14.13472514173469379,
\qquad
a:=\rho_1-1,
\qquad
R:=|a|\approx14.143565845726.
\tag{2}
\]

The first nontrivial zero pair `rho_1, \bar rho_1` is rigorously known to be simple and on the critical line, and it is the unique nearest singularity pair of `Q` about `w=0`.

Let `0<t_n<=1` be any real sequence with

\[
t_n\longrightarrow\tau\in(0,1],
\tag{3}
\]

and, for fixed `0<\alpha<1`, put `K_n=\lfloor\alpha n\rfloor` and define the damped initial source prefix

\[
\Lambda_n^{\le\alpha}(t_n)
:=
\sum_{k=1}^{K_n}\binom nk t_n^k b_{k-1}.
\tag{4}
\]

Then for every

\[
0<\alpha<\alpha_*(\tau)
:=\frac{\tau}{R+\tau},
\tag{5}
\]

one has the unconditional exact root-rate asymptotic

\[
\boxed{
\limsup_{n\to\infty}
\left|\Lambda_n^{\le\alpha}(t_n)\right|^{1/n}
=
\frac{e^{H(\alpha)}\tau^\alpha}{R^\alpha}
>1,
}
\tag{6}
\]

where

\[
H(\alpha)
=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha).
\tag{7}
\]

By contrast, if `K_n=o(n)` and `t_n` stays bounded, then the corresponding initial prefix satisfies

\[
\boxed{
\limsup_{n\to\infty}
\left|
\sum_{k=1}^{K_n}\binom nk t_n^k b_{k-1}
\right|^{1/n}
\le1.
}
\tag{8}
\]

Thus every asymptotically nonzero damping strength leaves a nonempty **linear-depth artifact window**: sublinear completed jets are root-rate invisible, while every sufficiently small fixed positive linear fraction has root rate strictly greater than one for a reason already supplied by a zero pair known to be RH-compatible.

For the endpoint-preserving schedules of AF-240--AF-242, `tau=1`, so

\[
\alpha_*(1)=\frac1{R+1}
\approx0.06603464535.
\tag{9}
\]

In particular, the entire moving-damping family of AF-242, including, for all sufficiently large `n`,

\[
t_n=1-c n^{-\beta},
\qquad c>0,
\qquad0<\beta<1,
\tag{10}
\]

retains exactly the same proven small-linear-prefix obstruction as the undamped completed jet of AF-238. Slow return to the Li endpoint repairs the **full orbit**, not the source-depth truncation.

The result does not say that `6.6%` of the completed jet is sufficient. It says only that every fixed fraction below the threshold in `(9)` is already ruled out by a known critical-line pair. Larger fractions may still fail through interior-saddle cancellation or other zero contributions.

## Nearest-pole decomposition

Because `rho_1` and `\bar rho_1` are the unique nearest zeros of `xi` to `s=1`, there is `R_2>R` such that

\[
Q(w)
=
\frac1{w-a}
+
\frac1{w-\bar a}
+C(w),
\tag{11}
\]

with `C` analytic on `|w|<R_2`. Hence

\[
b_{k-1}
=-a^{-k}-\bar a^{-k}+c_{k-1},
\tag{12}
\]

where the coefficients of `C` have a strictly larger radius of analyticity.

The contribution of one nearest pole to `(4)` is

\[
T_{n,K}(a;t_n)
:=
\sum_{k=1}^{K}\binom nk\left(\frac{t_n}{a}\right)^k.
\tag{13}
\]

Take `K=K_n`. If

\[
u_{n,k}:=\binom nk\left(\frac{t_n}{a}\right)^k,
\]

then for each fixed `r>=0`,

\[
\frac{u_{n,K_n-r}}{u_{n,K_n}}
\longrightarrow
\left(
\frac{\alpha a}{\tau(1-\alpha)}
\right)^r.
\tag{14}
\]

Condition `(5)` is exactly

\[
\left|
\frac{\alpha a}{\tau(1-\alpha)}
\right|<1.
\tag{15}
\]

Moreover the reversed ratios are uniformly bounded by a number below one for all sufficiently large `n`. Therefore the retained prefix is endpoint dominated and geometric summation gives

\[
\frac{T_{n,K_n}(a;t_n)}
{\binom n{K_n}(t_n/a)^{K_n}}
\longrightarrow
C_{\alpha,\tau}
:=
\left(
1-\frac{\alpha a}{\tau(1-\alpha)}
\right)^{-1}.
\tag{16}
\]

No regularity of the increments `t_{n+1}-t_n` is needed. Only the nonzero limit `tau` enters this source-prefix asymptotic.

## The known critical-line pair cannot cancel the endpoint rate

Write `a=R e^{i\theta}`. Adding the conjugate pole in `(12)` yields

\[
-2\binom n{K_n}
 t_n^{K_n}R^{-K_n}
\left(
\Re\!\left(C_{\alpha,\tau}e^{-iK_n\theta}\right)
+o(1)
\right).
\tag{17}
\]

Since `0<alpha<1`, the sequence `K_n=floor(alpha n)` visits every sufficiently large integer. The nonzero complex sequence

\[
\Re\!\left(C_{\alpha,\tau}e^{-ik\theta}\right)
\tag{18}
\]

therefore has an infinite subsequence bounded away from zero: if `theta/pi` is rational this follows from its finite nondegenerate orbit, and if it is irrational it follows from density on the circle. The fact that `a` is nonreal excludes the only two-point degeneracy that could make all real parts vanish.

Stirling's formula and `t_n->tau` now give

\[
\limsup_{n\to\infty}
\left|
\text{nearest-pair prefix}
\right|^{1/n}
=
\frac{e^{H(\alpha)}\tau^\alpha}{R^\alpha}.
\tag{19}
\]

This is already a structural warning: the exponential prefix is generated by a pair known to satisfy the RH location constraint.

## The analytic remainder is exponentially smaller

Choose `R'` with

\[
R<R'<R_2
\qquad\text{and}\qquad
\alpha<\frac{\tau}{R'+\tau},
\tag{20}
\]

which is possible by the strict inequality `(5)`. Cauchy's estimate gives

\[
|c_j|\le M_{R'}(R')^{-j}.
\tag{21}
\]

For all sufficiently large `n`, the corresponding damped binomial prefix is again endpoint dominated, now with `R'` in place of `R`. Consequently

\[
\limsup_{n\to\infty}
\left|
\sum_{k=1}^{K_n}\binom nk t_n^k c_{k-1}
\right|^{1/n}
\le
\frac{e^{H(\alpha)}\tau^\alpha}{(R')^\alpha}
<
\frac{e^{H(\alpha)}\tau^\alpha}{R^\alpha}.
\tag{22}
\]

The remainder cannot cancel the nearest-pair limsup, so `(6)` follows.

Finally put

\[
f_\tau(\alpha)
:=H(\alpha)+\alpha\log\frac\tau R.
\tag{23}
\]

For the range `(5)`,

\[
f_\tau'(\alpha)
=
\log\frac{\tau(1-\alpha)}{\alpha R}>0,
\tag{24}
\]

while `f_tau(0+)=0`. Hence the root rate in `(6)` is strictly greater than one throughout the entire proved artifact window.

## Sublinear depth remains invisible

Because `Q` is analytic at `w=0`, its coefficients obey an exponential bound

\[
|b_j|\le C A^j
\tag{25}
\]

for fixed constants `C,A`. If `t_n` is bounded and `K_n=o(n)`, then

\[
\left|
\sum_{k=1}^{K_n}\binom nk t_n^k b_{k-1}
\right|
\le
C K_n
\exp\!\left[
K_n\log\frac{en}{K_n}+O(K_n)
\right].
\tag{26}
\]

Writing `alpha_n=K_n/n`, the normalized logarithm is at most

\[
\alpha_n\log\frac{C'}{\alpha_n}+o(1)
\longrightarrow0,
\tag{27}
\]

which proves `(8)`. This is the completed-and-damped analogue of the AF-236 sublinear information-price obstruction.

## The missing tail performs essential cancellation even for a known RH-compatible pair

For the pole corresponding to one zero `rho`, the **full** damped binomial orbit is exactly

\[
-\sum_{k=1}^n\binom nk
\left(\frac{t_n}{\rho-1}\right)^k
=
1-\left(1+\frac{t_n}{\rho-1}\right)^n.
\tag{28}
\]

Equivalently, after relabeling the symmetric zero set by `rho -> 1-rho`, the global zero sum may be written in the AF-239--AF-242 form `1-(1-t_n/rho)^n`. For a specific critical-line zero it is cleaner to keep the pole coordinate in `(28)`. If `rho=1/2+i gamma` and `0<t_n<=1`, then

\[
\left|1+\frac{t_n}{\rho-1}\right|^2
=
1-\frac{t_n(1-t_n)}{|\rho-1|^2}
\le1.
\tag{29}
\]

Thus the complete contribution of the rigorously known first critical-line pair has root rate at most one, whereas its prefix in `(17)` has root rate strictly greater than one throughout `(5)`. The omitted tail `k>K_n` must therefore cancel an exponentially larger prefix merely to restore the harmless full-orbit behavior of a zero that is already on the critical line.

This is stronger than saying that truncation might lose a hypothetical off-critical signal. The deep source terms are demonstrably required to cancel a **known admissible signal** before the Li root-rate quotient can even be interpreted correctly.

## Prior art and novelty assessment

The completed function and Li/Keiper differential and generating-function representations are classical. Jerry B. Keiper, **“Power Series Expansions of Riemann's xi Function,”** *Mathematics of Computation* 58 (1992), 765--773, DOI `10.1090/S0025-5718-1992-1122072-5`, is the primary source for the local `xi` power-series viewpoint used by the Li coefficients.

Pedro Freitas, **“A Li-Type Criterion for Zero-Free Half-Planes of Riemann's Zeta Function,”** *Journal of the London Mathematical Society* 73 (2006), 399--414, DOI `10.1112/S0024610706022599`, studies full parameterized Li families and their zero-free-strip meaning. Mark W. Coffey, **“New results concerning power series expansions of the Riemann xi function and the Li/Keiper constants,”** *Proceedings of the Royal Society A* 464 (2008), 711--731, DOI `10.1098/rspa.2007.0212`, develops the local-coefficient/binomial structure around the Li constants. André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`, gives the classical RH/off-RH asymptotic dichotomy for Li coefficients.

The nearest-zero input is justified by rigorous critical-line verification; Dave Platt and Tim Trudgian, **“The Riemann hypothesis is true up to `3·10^12`,”** *Bulletin of the London Mathematical Society* 53 (2021), 792--797, DOI `10.1112/blms.12460`, supplies much stronger verified height than needed here.

A targeted audit found the established full parameterized Li criteria and local Li/xi coefficient literature, but no source was used to support a novelty claim for the moving-weight **truncated** binomial theorem `(6)`. Endpoint asymptotics for incomplete binomial sums are classical, and `(6)` is a direct extension of the AF-238 nearest-pole argument. **No literature novelty is claimed.** The durable result is the source-fidelity consequence: asymptotically nonzero damping cannot by itself turn small linear completed-jet prefixes into faithful Li root-rate surrogates.

## Exact controls and boundaries

**AF-238 control.** Setting `t_n=1` gives `tau=1` and recovers exactly the AF-238 small-linear completed-jet root rate and threshold.

**AF-242 control.** Every schedule covered by AF-242 has `t_n->1`, so all of them inherit `(9)` independently of the slow-modulation condition that makes the full orbit faithful. The two theorems concern different operations: AF-242 preserves cancellation after summing all `n` source orders; AF-243 shows that truncating that sum reopens the nearest-pole artifact.

**Fixed-damping control.** If `t_n->tau<1`, the artifact interval shrinks to `alpha<tau/(R+tau)` but remains nonempty for every `tau>0`. Sending the damping limit toward zero is the only way this particular proved prefix window can collapse to zero, but AF-239 shows that fixed positive damping already changes the decoded zero-free band, and `tau=0` is not the Li endpoint.

**Threshold is not sufficiency.** Equation `(5)` is the endpoint-dominance boundary of this proof. It is not a theorem that prefixes above it are faithful. Interior saddle points and farther singularities can still create or destroy exponential behavior.

**No prime-side compression yet.** The finding prices source depth only in the canonical completed local-jet coordinate. It does not prove that every possible representation needs linear information, nor that prime-side data cannot be aggregated nonlocally before entering the Li transform.

**No RH assumption.** The exponential prefix rate uses only a zero pair already rigorously located on the critical line. The theorem neither assumes nor supplies evidence for RH.

## Consequences for the research frontier

The Li source-access problem now has a sharper two-sided obstruction in the canonical local coordinate. Sublinear source depth is erased by the root-rate quotient, while a whole positive interval of fixed linear depths is contaminated by an exponentially large contribution from a known critical-line zero pair. A successful source reduction therefore cannot be justified merely by making `t_n` approach the Li endpoint smoothly.

The next viable route must change **how source orders are grouped**, not just their scalar weights. Candidates should preserve complete cancellation orbits by construction—for example block/orbit completion, a contour/global transform, or another non-prefix aggregation—and then prove that the resulting source statistic is genuinely cheaper than carrying the full local jet while retaining the AF-235 root-rate discriminator. The first test for any such proposal is whether the known pair `rho_1,\bar rho_1` remains root-rate neutral after the proposed compression.