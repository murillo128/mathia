# AF-242 — slowly varying Li damping removes the second-order barrier

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `RH-SUFFICIENT-QUOTIENT`, `CANCELLATION-COHERENCE`, `SCALE-DEPENDENT-FILTER`, `TARGET-METRIC`, `NO-NOVELTY-CLAIM`

## Claim

AF-241 proves that mesoscopic damping preserves the ordinary Li root-rate discriminator while suppressing every fixed critical-line zero, but its proof assumes the sufficient second-order restriction

\[
n(1-t_n)^2\to0.
\]

That restriction is not intrinsic to the moving-damping mechanism. It can be removed completely if the schedule itself varies slowly enough from one index to the next.

Let

\[
Q(w):=\frac{\xi'}{\xi}(1+w)=\sum_{j\ge0}b_jw^j,
\qquad
\Lambda_n(t):=\sum_{k=1}^n\binom nk t^k b_{k-1},
\tag{1}
\]

and write

\[
\varepsilon_n:=1-t_n.
\tag{2}
\]

Assume a deterministic real schedule satisfies

\[
0<t_n\le1,
\qquad
\varepsilon_n\to0,
\qquad
n\,|\varepsilon_{n+1}-\varepsilon_n|\to0.
\tag{3}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\limsup_{n\to\infty}|\Lambda_n(t_n)|^{1/n}\le1.
}
\tag{4}
\]

If RH is false and

\[
q:=\max_\rho\left|1-\frac1\rho\right|>1,
\tag{5}
\]

then in fact

\[
\boxed{
\limsup_{n\to\infty}|\Lambda_n(t_n)|^{1/n}=q.
}
\tag{6}
\]

Thus every schedule satisfying `(3)` has exactly the ordinary Li exponential decoder even when higher powers such as `n\varepsilon_n^2` diverge.

If, in addition,

\[
n\varepsilon_n\to\infty,
\tag{7}
\]

then every fixed critical-line zero `\rho=1/2+i\gamma` is strongly suppressed:

\[
\boxed{
\left|1-\frac{t_n}{\rho}\right|^n
=
\exp\!\left(
-\frac{n t_n\varepsilon_n}{2|\rho|^2}(1+O(\varepsilon_n))
\right)
\longrightarrow0.
}
\tag{8}
\]

Consequently the explicit power family

\[
t_n=1-c n^{-\alpha},
\qquad c>0,
\qquad 0<\alpha<1,
\tag{9}
\]

for all sufficiently large `n`, simultaneously suppresses every fixed RH-compatible zero orbit and preserves the exact RH root-rate class. AF-241 had established only the subrange `1/2<\alpha<1`; the apparent `\alpha=1/2` boundary was an artifact of first-order truncating the moving logarithm rather than a fidelity barrier.

This result closes the first of the two frontier questions left by AF-241 at the level of a broad sufficient regularity class: the second-order condition can be discarded. It does **not** classify all possible moving schedules, and it does not solve the separate source-access/compression problem.

## Zero-sum representation

As in AF-239--AF-241, symmetric Hadamard ordering gives

\[
\Lambda_n(t)
=
\sum_\rho
\left[
1-\left(1-\frac t\rho\right)^n
\right],
\tag{10}
\]

with multiplicity and the standard symmetric pairing understood.

Under RH, AF-240 already proves the uniform estimate

\[
0\le \Lambda_n(t)\le C_\xi(n^2+n)
\qquad (0\le t\le1),
\tag{11}
\]

so the forward implication in `(4)` holds for arbitrary moving schedules in `[0,1]`. Only the false-RH direction needs a new argument.

## Exact slow-modulation argument for the dominant off-critical shell

Assume RH is false and set

\[
u_\rho:=1-\frac1\rho.
\tag{12}
\]

As established in AF-240/AF-241, reflection symmetry produces `q>1` in `(5)`, the maximum is attained, and the dominant set

\[
M:=\{\rho:|u_\rho|=q\}
\tag{13}
\]

is finite and nonempty. Put

\[
z_\rho:=\frac{u_\rho}{q},
\qquad |z_\rho|=1.
\tag{14}
\]

The map `\rho\mapsto1-1/\rho` is injective, so the `z_\rho` for distinct zero locations in `M` are distinct.

For sufficiently large `n`, define on a fixed neighborhood of `0`

\[
f_\rho(\varepsilon)
:=
\operatorname{Log}\!\left(1+\frac{\varepsilon}{\rho-1}\right),
\tag{15}
\]

using the analytic logarithm with `f_\rho(0)=0`, and let

\[
h_{\rho,n}:=n f_\rho(\varepsilon_n).
\tag{16}
\]

The zero factor is now represented **exactly**, without expanding in powers of `\varepsilon_n`:

\[
\left(1-\frac{t_n}{\rho}\right)^n
=
q^n z_\rho^n e^{h_{\rho,n}}.
\tag{17}
\]

Because `M` is finite, all `f_\rho'` are uniformly bounded near zero. From `(3)`,

\[
\begin{aligned}
h_{\rho,n+1}-h_{\rho,n}
&=f_\rho(\varepsilon_{n+1})
+n\bigl[f_\rho(\varepsilon_{n+1})-f_\rho(\varepsilon_n)\bigr],
\end{aligned}
\tag{18}
\]

and therefore

\[
\max_{\rho\in M}|h_{\rho,n+1}-h_{\rho,n}|\to0.
\tag{19}
\]

This is the key replacement for AF-241's first-order expansion. The entire exact amplitude and phase correction is slowly varying; no condition on `n\varepsilon_n^2`, or on any higher power `n\varepsilon_n^k`, is required.

Normalize the moving amplitudes by

\[
R_n:=\max_{\rho\in M}\Re h_{\rho,n},
\qquad
d_{\rho,n}:=e^{h_{\rho,n}-R_n}.
\tag{20}
\]

Then

\[
|d_{\rho,n}|\le1,
\qquad
\max_{\rho\in M}|d_{\rho,n}|=1.
\tag{21}
\]

Since the maximum is over a finite set, `(19)` also gives

\[
|R_{n+1}-R_n|\to0,
\qquad
\max_{\rho\in M}|d_{\rho,n+1}-d_{\rho,n}|\to0.
\tag{22}
\]

Let `m_\rho` be the multiplicity of `\rho` and define the normalized dominant exponential sum

\[
S_n:=\sum_{\rho\in M}m_\rho d_{\rho,n}z_\rho^n.
\tag{23}
\]

For `\rho\ne\sigma`, put `w_{\rho\sigma}=z_\rho\overline{z_\sigma}\ne1`. The coefficient

\[
a_n:=m_\rho m_\sigma d_{\rho,n}\overline{d_{\sigma,n}}
\]

is bounded and satisfies `a_{n+1}-a_n\to0`. Since the partial sums of `w_{\rho\sigma}^n` are uniformly bounded, summation by parts yields

\[
\frac1N\sum_{n\le N}a_n w_{\rho\sigma}^n\to0.
\tag{24}
\]

Indeed the numerator is bounded by a constant times

\[
1+\sum_{n<N}|a_{n+1}-a_n|=o(N).
\]

Expanding the mean square in `(23)`, all off-diagonal terms vanish by `(24)`, while at every `n` at least one `|d_{\rho,n}|` equals `1`. Hence

\[
\liminf_{N\to\infty}
\frac1N\sum_{n\le N}|S_n|^2
\ge1.
\tag{25}
\]

In particular,

\[
\limsup_{n\to\infty}|S_n|\ge1.
\tag{26}
\]

The dominant shell therefore cannot be annihilated by a slowly varying damping schedule.

Finally, because `f_\rho(\varepsilon)=O(\varepsilon)` uniformly on the finite set `M`,

\[
R_n=O(n\varepsilon_n)=o(n),
\tag{27}
\]

so

\[
(e^{R_n})^{1/n}\to1.
\tag{28}
\]

Combining `(17)`, `(23)`, `(26)`, and `(28)`, the dominant shell has root rate exactly `q` along a subsequence.

## Nondominant zeros stay below the dominant root rate

The remainder estimate used in AF-240/AF-241 needs only `t_n\to1`, not the discarded second-order condition.

Choose

\[
1<q_0<q_1<q.
\tag{29}
\]

Only finitely many zeros satisfy `|u_\rho|>q_0`; place them in a finite set `F` containing `M`. Since

\[
\left|\left(1-\frac{t_n}{\rho}\right)-u_\rho\right|
=\frac{\varepsilon_n}{|\rho|}
\tag{30}
\]

and nontrivial zeros stay a positive distance from the origin, all sufficiently large `n` satisfy

\[
\left|1-\frac{t_n}{\rho}\right|\le q_1
\tag{31}
\]

for every `\rho\notin F` with `|\Im\rho|\le2n`. The classical count `N(T)=O(T\log T)` bounds this part by

\[
O(n\log n\,q_1^n).
\tag{32}
\]

For `|\Im\rho|>2n`, conjugate pairing and the large-zero binomial expansion give, uniformly for `0<t_n\le1`,

\[
\left|
2\left(1-\Re\left(1-\frac{t_n}{\rho}\right)^n\right)
\right|
\ll\frac{n^2}{|\rho|^2}.
\tag{33}
\]

Partial summation from the zero count gives a total high-zero tail `O(n\log n)`. Every zero in the finite set `F\setminus M` has ordinary exponential rate strictly below `q`, while its moving correction has `n`th root tending to one.

Because `e^{R_n}=e^{o(n)}`, both `(32)` and the polynomial tail are exponentially negligible compared with `q^n e^{R_n}`. Together with `(26)`, this proves the lower bound in `(6)`; the same decomposition gives the upper bound. Thus `(6)` and `(4)` follow.

## Fixed critical-line suppression needs only first-order accumulated damping

For `\rho=1/2+i\gamma`, there is the exact identity

\[
\left|1-\frac{t_n}{\rho}\right|^2
=1-\frac{t_n\varepsilon_n}{|\rho|^2}.
\tag{34}
\]

Since `\varepsilon_n\to0`, taking logarithms gives

\[
\begin{aligned}
n\log\left|1-\frac{t_n}{\rho}\right|
&=-\frac{n t_n\varepsilon_n}{2|\rho|^2}
\bigl(1+O(\varepsilon_n)\bigr).
\end{aligned}
\tag{35}
\]

The error in `(35)` is relative, not an independently required `o(1)` additive error. Therefore `(7)` alone forces the exponent to `-\infty`; the fact that `n\varepsilon_n^2` may diverge is irrelevant to suppression. This proves `(8)`.

For the power schedule `(9)`,

\[
n|\varepsilon_{n+1}-\varepsilon_n|
\sim c\alpha n^{-\alpha}\to0,
\qquad
n\varepsilon_n=c n^{1-\alpha}\to\infty,
\tag{36}
\]

for every `0<\alpha<1`. Thus the entire open interval `(0,1)` is a cancellation-coherent RH-fidelity regime for this family.

The same theorem also admits much slower returns such as `\varepsilon_n=1/\log n`: the damping can be macroscopically larger than the AF-241 window while remaining sublinear in the exponent and slowly varying enough not to synthesize destructive high-frequency modulation.

## Prior art and novelty assessment

The fixed-parameter Li and generalized-Li frameworks are classical. Keiper's 1992 generating function, Bombieri--Lagarias' 1999 multiset criterion, Freitas' 2006 parameterized zero-free-half-plane criterion, and Voros' 2006 asymptotic dichotomy provide the established background used by AF-235 and AF-239--AF-241.

There is also explicit prior art for allowing the **generalized-Li parameter to depend on an index**. Sergey Sekatskii, *First applications of generalized Li's criterion to study the Riemann zeta-function zeroes location*, arXiv:`1404.7276` (2014), proves that for each finite cutoff `n` one can choose a parameter `b_n` large enough that the generalized-Li inequalities hold for all indices up to that cutoff. His earlier generalized criterion is arXiv:`1304.7895` (2013), later published in *Ukrainian Mathematical Journal*. This prevents treating the mere idea of an `n`-dependent Li parameter as new.

The targeted audit also checked the fixed-parameter generalized-Li literature represented by Freitas, Sekatskii, later `tau`-Li zero-free-region work, and recent surveys/variants. No audited source was used to support an existing theorem with the exact asymptotic schedule `(3)` or the slow-modulation mean-square argument `(18)--(26)`. **No novelty is claimed.** If an equivalent moving-parameter root-rate theorem is located, this finding should be reclassified as a specialization or rediscovery.

The durable Arithmetic Fidelity contribution is narrower: AF-241's apparent second-order boundary is removed by retaining the exact logarithmic modulation and auditing what regularity is actually needed to prevent the compression/filter from cancelling its own discriminator.

## Exact controls and boundaries

**AF-241 control.** AF-241 assumes `n\varepsilon_n^2\to0` and `n\varepsilon_n\to\infty`. Every such sufficiently regular schedule is contained here, but `(3)` also permits `n\varepsilon_n^2\to\infty`.

**Power-law control.** `\varepsilon_n=c n^{-\alpha}` with `0<\alpha<1/2` explicitly violates AF-241's second-order condition while satisfying `(3)` and `(7)`. It is therefore a genuine new regime covered by the exact modulation proof.

**Fixed-damping control.** A fixed `\varepsilon>0` violates `\varepsilon_n\to0`; AF-239 applies and the discriminator loses a nonzero strip adjacent to the critical line.

**Rapid-modulation boundary.** The theorem does not cover arbitrary `t_n\to1`. An `O(1/n)` perturbation in `t_n` can create an order-one phase perturbation in a fixed dominant zero factor, so an adversarial rapidly varying schedule can in principle target exponential-shell cancellation. Condition `(3)` is a clean source-side sufficient regularity gate; it is not claimed necessary or sharp.

**No source-depth saving.** `\Lambda_n(t_n)` still consumes the full local jet `b_0,\ldots,b_{n-1}`. The theorem improves the filter-classification side of AF-241 but does not reduce the source-access bill from AF-236.

**No proof of RH.** Equation `(4)` is an equivalence. Nothing here establishes the subexponential root-rate bound unconditionally.

## Consequences for the research frontier

AF-241 separated the moving-filter problem from the actual compression problem. AF-242 now removes its main artificial filter restriction: there is a large regular class of schedules, including every power return `1-t_n\asymp n^{-\alpha}` with `0<\alpha<1`, that suppresses each fixed critical-line orbit while preserving the exact off-RH exponential rate.

The important remaining question is therefore no longer how delicately the damping must approach `1`. The unresolved bill is **source access**. All these filters still require the complete depth-`n` local `\xi'/\xi` jet, so they have not compressed the arithmetic source at all. A genuinely useful next result should either construct a cheaper source-side representation that realizes the same moving height horizon while completing the cancellations before the root-rate quotient, or prove that any representation with materially sublinear source access necessarily loses that RH discriminator.
