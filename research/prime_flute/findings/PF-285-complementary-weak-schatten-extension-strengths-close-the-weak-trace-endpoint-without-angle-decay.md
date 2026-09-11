# PF-285 — complementary weak-Schatten extension strengths close the weak-trace endpoint without angle decay

**Status:** `EXACT-DERIVED + CLASSICAL-SINGULAR-VALUE-CALCULUS + WEAK-SCHATTEN-PRODUCT + POSITIVE/ROUTE-SHARPENING`.

[[research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle|PF-282]] gives the exact physical factorization

\[
T=F_P\Gamma F_H,
\qquad
F_P=f(|R_P|),\quad F_H=f(|R_H|),\quad
f(t)=\frac{t}{\sqrt{1+t^2}},
\qquad \|\Gamma\|\le1.
\]

PF-283 then gives a sufficient endpoint criterion in terms of the thresholded heavy-angle count, while PF-284 proves that this criterion is not necessary and leaves a genuine interval between the `\tau^{-1}` sufficient count and the `\tau^{-3}` necessary symmetric envelope.

There is a second exact endpoint route inside the same factorization which does not require any angular decay at all. If the two extension-strength factors themselves have complementary weak-Schatten decay, their product already pays the full weak-trace budget. Concretely, if

\[
F_P\in\mathcal S_{p,\infty},
\qquad
F_H\in\mathcal S_{q,\infty},
\qquad
\frac1p+\frac1q\ge1,
\]

for finite `p,q\ge1`, then

\[
\boxed{T\in\mathcal S_{1,\infty}}
\]

for every bounded angle operator `\Gamma`. Equivalently, it is enough that the two heavy-strength populations satisfy

\[
\operatorname{rank}Q_P^\tau=O(\tau^{-p}),
\qquad
\operatorname{rank}Q_H^\tau=O(\tau^{-q}),
\qquad
\frac1p+\frac1q\ge1.
\]

The balanced critical case is especially important:

\[
\boxed{
F_P,F_H\in\mathcal S_{2,\infty}
\Longrightarrow
T\in\mathcal S_{1,\infty}.}
\]

Thus a `\tau^{-2}` heavy population on **both** physical sides is compatible with the desired endpoint even when the low-fed and high-fed extension ranges are maximally aligned. This is invisible to PF-283's rank-only heavy-angle sufficient test, which would see only a `\tau^{-2}` angle compression and therefore fail.

An explicit diagonal model realizes exactly that gap. With

\[
F_P=F_H=\operatorname{diag}((n+1)^{-1/2}),
\qquad
\Gamma=I,
\]

one has

\[
T=\operatorname{diag}((n+1)^{-1})\in\mathcal S_{1,\infty},
\]

but

\[
N_{\Gamma_\tau}(2\tau)\asymp\tau^{-2}
\qquad(\tau\downarrow0),
\]

so the PF-283 statistic `\tau N_{\Gamma_\tau}(2\tau)` diverges. PF-284's necessary budget remains satisfied because `\tau^3N_{\Gamma_\tau}(2\tau)\asymp\tau\to0`.

This changes the geometric order of attack on the live prime-flute endpoint. Before attempting a difficult principal-angle Weyl law, one should first estimate the two physical extension-strength populations separately. If their reciprocal population exponents already add to one, the endpoint closes with no angle theorem. Only the remaining exponent deficit must be supplied by angular decay.

## Claim

Let `\mathcal H_P,\mathcal H_H,\mathcal E` be Hilbert spaces. Let

\[
F_P:\mathcal H_P\to\mathcal H_P,
\qquad
F_H:\mathcal H_H\to\mathcal H_H
\]

be compact positive contractions and let

\[
\Gamma:\mathcal H_H\to\mathcal H_P
\]

be bounded. Put

\[
T:=F_P\Gamma F_H.
\tag{1}
\]

Suppose for finite `p,q\ge1` there are constants `C_P,C_H` such that

\[
s_n(F_P)\le C_P n^{-1/p},
\qquad
s_n(F_H)\le C_H n^{-1/q}.
\tag{2}
\]

Set

\[
\sigma:=\frac1p+\frac1q.
\tag{3}
\]

Then

\[
\boxed{
s_n(T)=O(n^{-\sigma}).}
\tag{4}
\]

In particular, if `\sigma\ge1`, then

\[
\boxed{T\in\mathcal S_{1,\infty}.}
\tag{5}
\]

If one strength factor is only bounded while the other already lies in `\mathcal S_{1,\infty}`, conclusion (5) follows directly from the two-sided ideal property.

For the PF-282 strength projections

\[
Q_P^\tau=\mathbf1_{[\tau,1]}(F_P),
\qquad
Q_H^\tau=\mathbf1_{[\tau,1]}(F_H),
\tag{6}
\]

the singular-value hypotheses (2) are equivalent, up to constants and the irrelevant finite head, to

\[
\operatorname{rank}Q_P^\tau=O(\tau^{-p}),
\qquad
\operatorname{rank}Q_H^\tau=O(\tau^{-q})
\qquad(\tau\downarrow0).
\tag{7}
\]

Hence (7) with `1/p+1/q\ge1` is a purely population-based sufficient endpoint criterion.

More generally, if the global angle operator is itself compact with

\[
s_n(\Gamma)=O(n^{-1/r})
\tag{8}
\]

for some finite `r\ge1`, the same argument gives

\[
s_n(T)=O\!\left(n^{-(1/p+1/r+1/q)}\right).
\tag{9}
\]

Thus a sufficient three-currency condition is

\[
\boxed{
\frac1p+\frac1r+\frac1q\ge1.}
\tag{10}
\]

Equation (10) is only a convenient global sufficient rule. PF-283/PF-284 remain more flexible because they allow the angle decay to depend on the strength threshold instead of requiring `\Gamma` itself to lie in a weak Schatten class.

## 1. The product singular-value inequality gives the exponent addition

The classical singular-value product inequality says that for compact operators `A,B`,

\[
s_{m+n-1}(AB)\le s_m(A)s_n(B).
\tag{11}
\]

Also, multiplication by a bounded operator gives

\[
s_m(F_P\Gamma)\le \|\Gamma\|s_m(F_P).
\tag{12}
\]

For a target index `k\ge2`, choose positive integers `m,n` with

\[
m+n-1=k,
\qquad
m,n\ge k/2.
\tag{13}
\]

Applying (11) to `(F_P\Gamma)F_H`, then (12) and (2), yields

\[
\begin{aligned}
s_k(T)
&\le s_m(F_P\Gamma)s_n(F_H)\\
&\le \|\Gamma\|C_PC_H\,m^{-1/p}n^{-1/q}\\
&\le 2^\sigma\|\Gamma\|C_PC_H\,k^{-\sigma}.
\end{aligned}
\tag{14}
\]

This proves (4). When `\sigma\ge1`, equation (14) immediately gives

\[
\sup_k k\,s_k(T)<\infty,
\]

which is exactly weak trace class in the convention used throughout this line.

The three-factor statement (9) follows by applying (11) twice and splitting the target singular-value index among the three compact factors. No commutation, shared eigenbasis, or alignment assumption is used.

## 2. Heavy-population bounds are exactly weak-Schatten strength bounds

For a positive compact contraction `F`, let

\[
N_F(\tau)=\#\{n:s_n(F)\ge\tau\}.
\tag{15}
\]

The standard inversion between a decreasing singular-value sequence and its counting function gives

\[
s_n(F)=O(n^{-1/p})
\quad\Longleftrightarrow\quad
N_F(\tau)=O(\tau^{-p})
\qquad(\tau\downarrow0).
\tag{16}
\]

For the spectral projections (6),

\[
N_{F_P}(\tau)=\operatorname{rank}Q_P^\tau,
\qquad
N_{F_H}(\tau)=\operatorname{rank}Q_H^\tau.
\tag{17}
\]

Thus the actual prime-flute geometry need not first solve a principal-angle problem. A census of the low-fed and high-fed extension strengths already decides whether the two outer factors close the endpoint by themselves.

The critical balanced population law is

\[
\operatorname{rank}Q_P^\tau,
\operatorname{rank}Q_H^\tau
=O(\tau^{-2}).
\tag{18}
\]

Each side is then only weak Hilbert--Schmidt, but the two strengths multiply through an arbitrary bounded `\Gamma` to produce weak trace class.

## 3. PF-283's sufficient heavy-angle law can fail while the endpoint holds

Take `\mathcal H_P=\mathcal H_H=\ell^2(\mathbb N)` and

\[
F_Pe_n=F_He_n=(n+1)^{-1/2}e_n,
\qquad
\Gamma=I.
\tag{19}
\]

Then

\[
Te_n=(n+1)^{-1}e_n,
\tag{20}
\]

so `T\in\mathcal S_{1,\infty}` exactly at the endpoint.

For small `\tau`, each heavy projection in (6) has rank comparable to `\tau^{-2}`. Because the two projections are identical and `\Gamma=I`,

\[
\Gamma_\tau=Q_P^\tau Q_H^\tau=Q_P^\tau.
\tag{21}
\]

For `0<\tau<1/2`, every nonzero singular value of this projection equals one and therefore exceeds `2\tau`. Hence

\[
N_{\Gamma_\tau}(2\tau)
=\operatorname{rank}Q_P^\tau
\asymp\tau^{-2}.
\tag{22}
\]

Consequently

\[
\tau N_{\Gamma_\tau}(2\tau)\asymp\tau^{-1}\to\infty,
\tag{23}
\]

so PF-283's sufficient criterion fails, despite (20). At the same time

\[
\tau^3N_{\Gamma_\tau}(2\tau)\asymp\tau\to0,
\tag{24}
\]

which is fully consistent with PF-284's necessary symmetric envelope.

This is not merely a logical possibility. It identifies the concrete mechanism filling part of the PF-284 gap: **balanced strength damping can pay the endpoint budget even when the heavy-angle compression has no decay at all.**

## 4. The reciprocal-exponent boundary is sharp when the angle supplies no help

The same diagonal model gives the sharp worst-angle test. For finite `p,q\ge1`, set

\[
F_Pe_n=(n+1)^{-1/p}e_n,
\qquad
F_He_n=(n+1)^{-1/q}e_n,
\qquad
\Gamma=I.
\tag{25}
\]

Then

\[
Te_n=(n+1)^{-\sigma}e_n,
\qquad
\sigma=\frac1p+\frac1q.
\tag{26}
\]

If `\sigma<1`, then

\[
n\,s_n(T)=n^{1-\sigma}(1+o(1))\to\infty,
\]

so `T\notin\mathcal S_{1,\infty}`. Therefore no population-only theorem based solely on weak-`S_p` and weak-`S_q` control can improve the reciprocal condition without importing additional angular information.

When `\sigma<1`, equation (10) quantifies one sufficient form of the missing angular budget: a global weak-`S_r` estimate with

\[
\frac1r\ge1-\frac1p-\frac1q
\tag{27}
\]

would close the endpoint. Thresholded PF-283/PF-284 estimates may achieve the same compensation more economically and remain the preferred route when `\Gamma` is not globally compact.

## Relevance to the prime flute

The accepted variable-corridor clue currently asks for a heavy-angle Weyl law because PF-283 reduced the endpoint to such a sufficient count and PF-284 supplied the corresponding obstruction budget. The factorization already contains a cheaper first test.

For the actual simultaneous one-cusp-pant extension, estimate separately

\[
N_{F_P}(\tau)=\operatorname{rank}Q_P^\tau,
\qquad
N_{F_H}(\tau)=\operatorname{rank}Q_H^\tau.
\]

If the physical geometry gives polynomial envelopes with exponents `p_P,p_H` satisfying

\[
\frac1{p_P}+\frac1{p_H}\ge1,
\]

then PF-285 proves `T\in\mathcal S_{1,\infty}` without any principal-angle theorem. PF-281 then transfers that ideal membership to the mixed inverse block and the reciprocal-prime coefficient commutator.

If the reciprocal sum is below one, the deficit

\[
1-\frac1{p_P}-\frac1{p_H}
\]

is the amount of singular-value decay that the angle geometry must supply in a global weak-Schatten model. More refined thresholded angle estimates can still beat that global model, but they should be attacked only after the strength census shows that the outer factors do not already close the endpoint.

This preserves the distinction emphasized by the current Mind: reservoir strength and extension angle are separate currencies, and they should be budgeted together rather than forcing the entire endpoint through the angle count.

## Prior-art and novelty assessment

The operator-ideal mechanism is classical. The product singular-value inequality (11) is standard compact-operator calculus, and weak-Schatten Hölder inequalities are established prior art. A recent focused reference is Yi C. Huang and Sijie Luo, *On noncommutative Hölder inequality of Sukochev and Zanin for weak Schatten class*, arXiv:2403.17990 (2024), which discusses the weak-Schatten Hölder theorem and its sharp constants.

No novelty is claimed for weak-Schatten Hölder or for exponent addition under operator multiplication. The project-specific contribution is the exact specialization to PF-282's physical strength-angle factorization, the conversion of strength-population exponents into a directly checkable endpoint criterion, and the diagonal falsifier showing that PF-283's heavy-angle `O(\tau^{-1})` criterion can fail even when the PF-281 weak-trace target holds.

The proof above intentionally uses only the elementary singular-value inequality (11), so the project conclusion does not depend on optimal quasi-norm constants or on a delicate endpoint normalization convention.

## Boundary conditions and failure modes

This finding does **not** estimate the actual prime-flute extension-strength populations. In particular:

- the physical `F_P` or `F_H` may fail to be compact, in which case no finite polynomial heavy-population exponent exists and this route does not apply;
- a reciprocal exponent sum below one does not disprove the endpoint, because the angle operator may provide the missing decay;
- a failure of any global weak-Schatten model for `\Gamma` does not kill the thresholded PF-283 route;
- polynomial population bounds are sufficient bookkeeping, not a claim that the actual geometry must obey a pure power law;
- the diagonal models prove sharpness of the abstract population-only criterion, not that the canonical prime flute realizes those model spectra;
- no wave-operator, trace-formula, prime/clone separation, or RH consequence follows without the remaining geometric identification and the rest of the established reassembly chain.

The physical `P/H` split must remain fixed before estimating the strength spectra. Replacing it by a convenient mode decomposition can change `R_P,R_H` and therefore the very population exponents being tested.

## Decisive audit test

Re-derive (14) directly from the singular-value product inequality and verify the diagonal model (19)--(24). The model must simultaneously satisfy `T\in\mathcal S_{1,\infty}`, violate the PF-283 `\tau^{-1}` heavy-angle sufficient law, and remain inside the PF-284 necessary `\tau^{-3}` envelope.

For the canonical prime flute, construct the actual simultaneous pant-extension realization used by PF-282 and estimate the counting functions of the two bounded strength operators **before** estimating principal angles. If exponents `p_P,p_H` satisfy the reciprocal closure condition, the endpoint is proved through PF-285. Otherwise record the residual reciprocal deficit and test whether the physical angle operator supplies it globally or through the more flexible thresholded PF-283/PF-284 counts.