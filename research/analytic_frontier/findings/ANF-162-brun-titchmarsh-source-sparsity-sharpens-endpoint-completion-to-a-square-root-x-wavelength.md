# ANF-162 — Brun–Titchmarsh source sparsity sharpens endpoint completion to a square-root-X wavelength

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC-SECOND-MOMENT + ENDPOINT-SPECTRAL-SHARPENING + SHARP-INFORMATION-BOUNDARY`. `ANF-158` localized target-scale endpoint completion using only the pointwise bound `|r_X(n)| << log X`, leaving a critical cumulative rank `J_*=K sqrt(log X/X)` and a minimum physical support `sqrt(X/log X)`. The actual source is much sparser in quadratic mass than that worst coefficient class. For `r_X=vartheta-Q_R`, the Brun–Titchmarsh upper bound for primes in an interval and the small size of the rough counterterm imply the uniform source-specific estimate

\[
\sum_{n\in I}|r_X(n)|^2\ll |I|\log X
\]

on every interval `I subset [X,3X]` of length at least `sqrt(X/log X)`. Inserting this into the exact endpoint singular ledger of `ANF-158` removes the entire `sqrt(log X)` loss: only cumulative modes of rank `j=O(K/sqrt X)` can carry bow-scale endpoint completion, and their physical wavelength is `asymp sqrt X`. Conversely, this improved cutoff is sharp if one uses only the new local `L^2` information together with the existing pointwise bound. A target-scale endpoint completion also forces an actual twisted residual prefix or suffix of size `Omega(sqrt(X log X))` to extend across `Omega(sqrt X)` sites, improving the previous `Omega(sqrt(X/log X))` support requirement. Thus the remaining endpoint obstruction has a genuinely source-specific square-root-`X` spatial scale; carrier geometry and coefficient-size information alone no longer explain it.

## 1. The actual residual has only `O(H log X)` quadratic mass on every relevant endpoint interval

Retain the source-normal form of `ANF-149`,

\[
r_X(n)=\vartheta(n)-Q_R(n),
\qquad
Q_R(n)=c_R\,1_{(n,P(R))=1},
\qquad
c_R:=\frac{P(R)}{\varphi(P(R))},
\tag{1}
\]

with

\[
R=e^{(\log X)^{1/10}},
\qquad
c_R\ll\log R=(\log X)^{1/10}.
\tag{2}
\]

Here `vartheta(n)=log n` on primes and vanishes otherwise. Let `I` be any interval contained in `[X,3X]` with integer length `H` satisfying

\[
H\ge H_0(X):=\sqrt{\frac{X}{\log X}}.
\tag{3}
\]

The Brun–Titchmarsh interval bound gives, uniformly in the location of `I`,

\[
\#(I\cap\mathbb P)\ll \frac{H}{\log H}.
\tag{4}
\]

Because (3) implies `log H=(1/2+o(1))log X`, while every prime in `[X,3X]` has logarithm `asymp log X`,

\[
\sum_{n\in I}\vartheta(n)^2
\ll
\frac{H}{\log H}\log^2(3X)
\ll
H\log X.
\tag{5}
\]

The rough counterterm is even cheaper. From (1)--(2), without using any distribution theorem for rough numbers,

\[
\sum_{n\in I}Q_R(n)^2
\le
Hc_R^2
\ll
H(\log X)^{1/5}
=o(H\log X).
\tag{6}
\]

Therefore `|a-b|^2<=2|a|^2+2|b|^2` gives the uniform source-specific local second-moment bound

\[
\boxed{
\sum_{n\in I}|r_X(n)|^2\ll H\log X
}
\tag{7}
\]

for every interval satisfying (3). No information about the distinguished twist is used here. In particular multiplication by `n^{-iU}` leaves (7) unchanged.

This is strictly stronger than the coefficient-class estimate used in `ANF-158`, which bounded the same quadratic mass by `O(H log^2 X)` from `|r_X(n)|<<log X`. The saving is not a cancellation statement: it comes from the fact that the `log X`-sized positive coefficients occur only at primes, while the deterministic negative counterterm has size only `O((log X)^{1/10})`.

## 2. The dangerous cumulative rank drops from `K sqrt(log X/X)` to `K/sqrt X`

Use the exact integer endpoint notation of `ANF-158`. Thus `L=K-1`, the left and right edge vectors are

\[
e^-_n=b_n,
\qquad
e^+_n=b_{M+1-n},
\qquad 1\le n\le L,
\tag{8}
\]

where `b_n` is the exact twisted residual coefficient, and

\[
E_{\partial}(b)
=
\sum_{j=1}^{L}\lambda_j
\bigl(|\alpha_j^-|^2+|\alpha_j^+|^2\bigr),
\qquad
\lambda_j=
\frac{1}{4\sin^2((2j-1)\pi/(4L+2))}.
\tag{9}
\]

In the bow range

\[
K=X^{1-2\varepsilon+o(1)},
\qquad 0<\varepsilon<\frac14,
\tag{10}
\]

one has `K/H_0(X)->infinity`. Both endpoint coefficient blocks lie inside `[X,3X]`, so (7) with `H asymp K` yields

\[
\boxed{
\|e^-\|_2^2+\|e^+\|_2^2\ll K\log X.
}
\tag{11}
\]

Let `E_{>J}` be the contribution of modes `j>J` in (9). The exact monotonicity argument of `ANF-158` and its elementary eigenvalue bound give

\[
E_{>J}
\le
\lambda_{J+1}
\bigl(\|e^-\|_2^2+\|e^+\|_2^2\bigr)
\ll
\frac{K^3\log X}{J^2}.
\tag{12}
\]

Define the source-specific critical rank

\[
\boxed{
J_{\rm src}(X,K):=\frac{K}{\sqrt X}.
}
\tag{13}
\]

If `J=J_X<K` and

\[
\frac{J_X}{J_{\rm src}(X,K)}\longrightarrow\infty,
\tag{14}
\]

then (12) gives

\[
\boxed{
E_{>J_X}=o(XK\log X).
}
\tag{15}
\]

Thus target-scale endpoint completion can live only in a slowly enlarged initial segment of `K/sqrt X` cumulative sine modes. Compared with `ANF-158`,

\[
J_*(X,K)=K\sqrt{\frac{\log X}{X}},
\tag{16}
\]

the actual source second moment removes a factor `sqrt(log X)` from the dangerous rank.

In the bow regime (10),

\[
J_{\rm src}
=X^{1/2-2\varepsilon+o(1)},
\qquad
\frac{J_{\rm src}}K=X^{-1/2},
\tag{17}
\]

and the associated physical wavelength is

\[
\boxed{
\frac{K}{J_{\rm src}}\asymp\sqrt X.
}
\tag{18}
\]

So the endpoint obstruction is confined to modes that vary only on square-root-`X` or longer physical scales.

## 3. The improved rank is sharp from source quadratic mass alone

The scale (13) cannot be reduced using only (11) together with the existing pointwise bound. Fix `c>0`, choose

\[
j_X\sim c\frac{K}{\sqrt X},
\tag{19}
\]

and let `u_{j_X}` be the exact normalized cumulative sine eigenvector from `ANF-158`. Consider the synthetic edge control

\[
e^-:=\sqrt{K\log X}\,u_{j_X},
\qquad
e^+:=0.
\tag{20}
\]

Then

\[
\|e^-\|_2^2=K\log X,
\tag{21}
\]

while the exact normalization of `u_j` gives

\[
\|e^-\|_\infty=O(\sqrt{\log X}),
\tag{22}
\]

which is even smaller than the actual crude coefficient ceiling `O(log X)`. Since `j_X=o(K)` and `j_X->infinity`, the eigenvalue asymptotic from `ANF-158` gives

\[
\lambda_{j_X}
=(1+o(1))\frac{K^2}{\pi^2j_X^2}
=(1+o(1))\frac{X}{\pi^2c^2}.
\tag{23}
\]

Hence this one mode contributes

\[
\boxed{
E_{\partial}
=(1+o(1))\frac{1}{\pi^2c^2}XK\log X.
}
\tag{24}
\]

Therefore neither the local `L^2` scale (11) nor pointwise size information can make modes of rank `Theta(K/sqrt X)` harmless. This is an information-boundary control, not a model of the prime-minus-rough source: the actual arithmetic residual is not asserted to realize the sine packet (20).

## 4. A macroscopic endpoint correction now forces `Omega(sqrt X)` physical support

The same source second moment sharpens the physical-space formulation of `ANF-158`. Let

\[
M_{\partial}(b)
:=
\max_{1\le r<K}
\max\left\{
\left|\sum_{n=1}^{r}b_n\right|,
\left|\sum_{n=M-r+1}^{M}b_n\right|
\right\}.
\tag{25}
\]

The exact inequality from `ANF-158`,

\[
E_{\partial}(b)\le2(K-1)M_{\partial}(b)^2,
\tag{26}
\]

shows that if, for some fixed `delta>0`,

\[
E_{\partial}(b)\ge\delta XK\log X,
\tag{27}
\]

then

\[
M_{\partial}(b)
\ge
\left(\sqrt{\frac\delta2}+o(1)\right)
\sqrt{X\log X}.
\tag{28}
\]

Suppose the maximum is attained by a prefix or suffix of length `r`. The pointwise bound `|r_X(n)|<<log X` first forces

\[
r\gg\sqrt{\frac{X}{\log X}},
\tag{29}
\]

so the interval supporting that sum is in the range of (7). Cauchy--Schwarz and the unit modulus of the logarithmic twist then give

\[
M_{\partial}(b)^2
\le
r\sum_{n\in I_r}|r_X(n)|^2
\ll
r^2\log X.
\tag{30}
\]

Combining (28) and (30),

\[
\boxed{
r\gg_{\delta}\sqrt X.
}
\tag{31}
\]

Thus a target-scale endpoint completion cannot be created by a residual packet living only on the old `sqrt(X/log X)` support floor. It must remain coherently dangerous across at least square-root-`X` many endpoint sites. The physical support scale (31) and the spectral wavelength (18) now agree exactly to powers of `X` and logarithms.

This conclusion uses real source information but still does not rule the endpoint term out. A sequence with quadratic mass `asymp r log X` can in principle have a partial sum of order `r sqrt(log X)` by Cauchy--Schwarz, which reaches `sqrt(X log X)` precisely when `r asymp sqrt X`. Additional arithmetic decorrelation is therefore still necessary.

## 5. Consequence for the carrier-versus-source frontier

`ANF-159`--`ANF-161` showed that the exact logarithmic carrier can remain maximally coherent only up to the cubic scale `X^{1/3}`, and that every supercubic block has a power-saving vector-sum bound even inside the parity-quantized resonance tubes. The new source floor (31) lies still farther into that cancellation regime. At `L asymp sqrt X`, the estimate of `ANF-161` specializes to

\[
\left|
\sum_{j<L}
\exp(i[-U\log(M+j)+P_2(j)])
\right|
\ll
X^{5/12},
\tag{32}
\]

up to constants depending only on a fixed `U/X^2` window. Even after multiplying the whole block by one common coefficient of size `O(log X)`, this is

\[
O(X^{5/12}\log X)
=o(\sqrt{X\log X}).
\tag{33}
\]

Equation (33) is only a calibration: arbitrary variable residual coefficients can select favorable carrier phases, so it cannot be transferred to `r_X` without a weighted theorem. But it confirms that the newly sharpened critical packet is safely beyond every carrier-only resonance mechanism already identified.

The live endpoint gate can now be stated more economically. In the singular basis, it is enough to control the actual source coefficients

\[
\alpha_j^{\pm}
=
\langle e^{\pm},u_j\rangle
\tag{34}
\]

through a slowly enlarged range

\[
1\le j\le\omega(X)\frac{K}{\sqrt X},
\qquad \omega(X)\to\infty,
\tag{35}
\]

because (15) makes the complementary tail negligible. In physical space, any negative scenario must produce a distinguished-twist prefix or suffix spike of size `Omega(sqrt(X log X))` on a support of at least `Omega(sqrt X)`. These are equivalent views of the same remaining source-specific obstruction.

## 6. Prior-art boundary, stress tests, and next gate

The only new external input in this finding is classical. Montgomery and Vaughan's large-sieve proof of the Brun--Titchmarsh theorem gives the factor-two upper-bound scale for primes in an arbitrary interval; only the order-of-magnitude consequence `#(I cap P)<<H/log H` is used in (4). The deduction (5)--(7) for the Mathia residual and its insertion into the exact cumulative spectrum (9) are repository-specific consequences, not new prime-distribution theorems.

A neighboring fixed-interval result is Matomäki and Shao's discorrelation theorem for primes against polynomial phases on intervals `H=X^theta` with `theta>2/3`. It confirms that weighted prime cancellation becomes accessible on sufficiently long fixed intervals, but it does not cover the square-root-`X` support forced by (31), and it does not by itself control the combined prime-minus-`Q_R` residual. Thus no existing theorem found in the audit closes the new gate at `H asymp sqrt X`.

The stress tests are complementary. The synthetic sine packet (20) shows that (13) is sharp if one forgets the arithmetic placement of the source. Conversely, (31) uses only a one-sided implication: target-scale completion forces square-root support, but square-root support does not imply target-scale completion. The Brun--Titchmarsh input controls coefficient mass, not the signed twisted correlation. No statement here upgrades a density or mean-square estimate to exclusion of the bow target.

The next useful theorem should therefore exploit the **combined** source law `r_X=vartheta-Q_R` on square-root-`X` endpoint scales. One route is a bound

\[
\max_{\sqrt X\ll r<K}
\left|
\sum_{n<r}r_X(M+n)(M+n)^{-iU}
\right|
=o(\sqrt{X\log X}),
\tag{36}
\]

with the analogous right-edge estimate at the distinguished `U asymp X^2`. A potentially softer route is to control only the weighted low cumulative energy in (34)--(35), rather than every prefix separately. Either route must retain the prime--Ramanujan cancellation architecture of `ANF-149`; componentwise absolute bounds would discard precisely the arithmetic information still capable of beating the sharp information boundary (24).
