# WI-110 — Arbitrary linear rescue obeys a sharp conditioning--transmission product law

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes the scale-preserving part of the noninvertible/rectangular linear escape left open by WI-109. An arbitrary global linear source/target processing can make the WI-108/WI-109 full-packed concatenation well conditioned, even perfectly conditioned, but only by transmitting a proportion of the available operator/covariance scale that is at most the original vanishing singular-gap ratio. The tradeoff is exact and is attained by a Moore--Penrose right inverse or source whitening.

Let

\[
B:H_{\rm tar}\to H_{\rm src}
\tag{1}
\]

have full source row rank, with

\[
m:=\dim H_{\rm src},\qquad
r(B):=\frac{\sigma_m(B)}{\sigma_1(B)}.
\tag{2}
\]

Allow completely arbitrary finite-dimensional linear maps

\[
S:E\to H_{\rm tar},\qquad
L:H_{\rm src}\to F,
\tag{3}
\]

with no invertibility, squareness, block-diagonality, or dimension-preservation assumption. Put

\[
A=LBS.
\tag{4}
\]

If `rank(A)<m`, define `r_m(A)=0`. Otherwise set

\[
r_m(A):=\frac{\sigma_m(A)}{\sigma_1(A)}.
\tag{5}
\]

For nonzero `L,S`, define the scale-invariant normalized transmission

\[
\tau_B(L,S)
:=
\frac{\sigma_1(LBS)}
{\|L\|_2\,\sigma_1(B)\,\|S\|_2}.
\tag{6}
\]

Then every such pair satisfies the sharp product law

\[
\boxed{
r_m(LBS)\,\tau_B(L,S)\le r(B).
}
\tag{7}
\]

Consequently, if the processed system keeps a fixed relative singular gap

\[
r_m(LBS)\ge c>0,
\tag{8}
\]

then necessarily

\[
\boxed{
\tau_B(L,S)\le \frac{r(B)}{c}.
}
\tag{9}
\]

Conversely, if it transmits a fixed fraction `eta>0` of the natural bilinear operator scale,

\[
\tau_B(L,S)\ge\eta,
\tag{10}
\]

then

\[
\boxed{
r_m(LBS)\le\frac{r(B)}{\eta}.
}
\tag{11}
\]

Thus when `r(B)->0`, no arbitrary linear pre/post-processing can simultaneously preserve all `m` source directions, have a fixed relative condition gap, and transmit a fixed normalized amount of the original operator scale.

## 1. The product law is the singular-value ideal property

The only input is the classical ideal inequality for singular values. For every index `k`,

\[
\sigma_k(XYZ)
\le
\|X\|_2\,\sigma_k(Y)\,\|Z\|_2.
\tag{12}
\]

Applying (12) at `k=m` gives

\[
\sigma_m(LBS)
\le
\|L\|_2\,\sigma_m(B)\,\|S\|_2.
\tag{13}
\]

If `rank(A)<m`, (7) is immediate. Otherwise multiply (5) and (6):

\[
\begin{aligned}
r_m(A)\tau_B(L,S)
&=
\frac{\sigma_m(A)}{\sigma_1(A)}
\frac{\sigma_1(A)}
{\|L\|_2\sigma_1(B)\|S\|_2}\\
&=
\frac{\sigma_m(A)}
{\|L\|_2\sigma_1(B)\|S\|_2}\\
&\le
\frac{\sigma_m(B)}{\sigma_1(B)}
=r(B).
\end{aligned}
\tag{14}
\]

This proof does not know whether `S` is invertible, singular, rectangular, a partial isometry, a column selector, a cross-target mixer, or a pseudoinverse. Likewise `L` may be rectangular or singular provided the composition still retains rank `m`. The quantity `tau_B` is invariant under multiplying either `L` or `S` by a nonzero scalar, so the conclusion cannot be evaded by merely renormalizing the preprocessing operators.

There is also a direct one-sided proof useful for intuition. With `L=I`, choose a unit source vector `x` attaining `\|B^*x\|=\sigma_m(B)`. Then

\[
\|(BS)^*x\|
=\|S^*B^*x\|
\le\|S\|_2\sigma_m(B),
\tag{15}
\]

so `sigma_m(BS)<=||S|| sigma_m(B)`. A right compression may suppress the large singular directions enough to improve the **ratio** `sigma_m/sigma_1`, but it cannot lift the weakest source direction above the original weakest scale times its own operator norm. Equation (7) records exactly where the missing scale goes.

## 2. The bound is sharp, including for rectangular and singular escapes

A stronger blanket claim that arbitrary rectangular target processing cannot rescue conditioning would be false. Let `B^\dagger:H_src->H_tar` be the Moore--Penrose right inverse. Since `B` has full row rank,

\[
BB^\dagger=I_{H_{\rm src}},
\qquad
\|B^\dagger\|_2=\frac1{\sigma_m(B)}.
\tag{16}
\]

Take `L=I` and `S=B^\dagger`. Then

\[
r_m(BS)=1,
\qquad
\tau_B(I,B^\dagger)
=
\frac1{\sigma_1(B)\|B^\dagger\|_2}
=r(B),
\tag{17}
\]

so equality holds in (7). This is precisely the type of rectangular global target map that WI-109 deliberately left outside its invertible condition-number theorem: it produces a perfectly conditioned identity, but its normalized transmission is exactly the vanishing original gap.

Source whitening gives the same equality from the other side. With

\[
L_0=(BB^*)^{-1/2},\qquad S=I,
\tag{18}
\]

one has `L_0 B (L_0 B)^*=I`, hence `r_m(L_0B)=1`, while

\[
\|L_0\|_2=\frac1{\sigma_m(B)},
\qquad
\tau_B(L_0,I)=r(B).
\tag{19}
\]

Thus (7) is not an artifact of requiring invertibility or of measuring a condition number. Perfect global linear rescue is always available; what is impossible is perfect rescue **and** nonvanishing normalized transmission when the original gap vanishes. The theorem therefore identifies the exact boundary rather than overstating an impossibility.

## 3. Covariance/energy transmission also vanishes

The operator-scale statement has a trace-energy consequence closer to a covariance application. Define

\[
\mathcal E_B(L,S)
:=
\frac{\|LBS\|_F^2}
{m\,\|L\|_2^2\,\|B\|_2^2\,\|S\|_2^2}.
\tag{20}
\]

Since a rank-at-most-`m` operator satisfies

\[
\|A\|_F^2\le m\|A\|_2^2,
\tag{21}
\]

one has

\[
\mathcal E_B(L,S)\le\tau_B(L,S)^2.
\tag{22}
\]

Therefore a fixed relative gap (8) forces

\[
\boxed{
\mathcal E_B(L,S)
\le
\frac{r(B)^2}{c^2}.
}
\tag{23}
\]

Equivalently, if the processed covariance retains a fixed normalized trace-energy fraction `mathcal E_B>=eta^2`, then `tau_B>=eta` and hence

\[
\boxed{
r_m(LBS)\le\frac{r(B)}{\eta}.
}
\tag{24}
\]

This removes a possible normalization loophole in interpreting (7). A well-conditioned rectangular selector can indeed isolate and renormalize the weakest sector, but relative to the natural product scale of the original operator and the processing maps its entire output covariance must then collapse quadratically with the original singular-gap ratio.

## 4. Specialization to the full-packed Ramanujan counterfamily

Now let

\[
B=[\,G_1C_1\;\cdots\;G_JC_J\,]
\tag{25}
\]

be the already target-locally processed concatenation from WI-108, where the `C_j` are arbitrary and `B` retains full source row rank. On the simultaneous full-packed family of WI-107/WI-108,

\[
r(B)
\le
\varepsilon_{p,J}
:=
\sqrt{\frac{3(J-1)\Delta}{2p}},
\qquad
\Delta=q_J-q_1=O(J\log p).
\tag{26}
\]

After **any further global linear source map `L` and any global cross-target map `S`**, including singular or rectangular maps, (7) gives

\[
\boxed{
r_m(LBS)\,\tau_B(L,S)
\le
\sqrt{\frac{3(J-1)\Delta}{2p}}.
}
\tag{27}
\]

Hence under the same range

\[
J=o\!\left(\sqrt{\frac{p}{\log p}}\right),
\tag{28}
\]

the right-hand side tends to zero. In particular, any family with `r_m(LBS)>=c>0` must satisfy

\[
\tau_B(L,S)
=O_c\!\left(J\sqrt{\frac{\log p}{p}}\right)
\longrightarrow0,
\tag{29}
\]

and its normalized covariance energy satisfies

\[
\boxed{
\mathcal E_B(L,S)
=O_c\!\left(\frac{J^2\log p}{p}\right)
\longrightarrow0.
}
\tag{30}
\]

This is the missing scale-sensitive statement for the noninvertible/rectangular escape left by WI-109. A partial isometry that mixes or selects target columns may improve the condition ratio, but if it preserves all source dimensions then it can do so only inside a sector whose normalized transmitted scale vanishes as (29). A pseudoinverse may restore an identity, but it attains rather than violates the same tradeoff.

## 5. Boundaries and falsification controls

The theorem is a linear-algebraic obstruction on the exact full-packed interface, not a new asymptotic assertion about zeta zeros. The synchronized CRT family is still a uniform finite-window counterfamily; no positive analytic density of those windows is claimed.

More importantly, (7) does **not** say that a low-transmission sector is analytically useless. A future arithmetic argument could conceivably come with an external normalization or a weighted estimate that pays the reciprocal vanishing scale and still leaves a positive main term. Such a mechanism would be genuinely additional information. What (27)--(30) forbid is treating an arbitrary rectangular/singular global selector as a free coercivity improvement while silently forgetting how much operator or covariance scale it discards.

The result also does not constrain nonlinear processing, positive-slack information away from exact full packing, a target count at or above the first scale not excluded by WI-107/WI-108, or arithmetic structure that changes the input operator `B` before the full-packed compression. Those remain qualitatively distinct escapes.

Finally, nothing here identifies the uncertified zeta-zero complement. The finding narrows one proposed route for extracting more information from simultaneous Ramanujan defect blocks; it does not distinguish multiple critical-line zeros from off-line symmetric blocks or pure rank--trace slack.

## 6. Prior art and program consequence

The matrix inequality (12) is classical. It is the finite-dimensional Hilbert-space instance of the ideal property of singular values/approximation numbers; see R. A. Horn and C. R. Johnson, *Topics in Matrix Analysis*, Cambridge University Press, 1991, Chapter 3, and the classical `s`-number framework of A. Pietsch. WI-109 already uses the neighboring singular-value product inequalities for invertible condition-number transport.

A targeted audit also checked the restricted-invertibility and column-subset literature, beginning with J. Bourgain and L. Tzafriri, **Invertibility of “large” submatrices with applications to the geometry of Banach spaces and harmonic analysis**, *Israel Journal of Mathematics* 57 (1987), 137--224, DOI `10.1007/BF02772174`, together with rank-revealing/subset-selection work. That literature is the natural positive counterpart: one may often find a well-conditioned restriction after discarding directions. It does not contradict (7), because (7) insists on retaining all `m` source dimensions and keeps the transmitted scale in the accounting. No claim of novelty is made for the ideal inequality itself or for restricted-invertibility principles.

The durable consequence is the exact specialization to the WI-107/WI-108 counterfamily. WI-109 showed that an **invertible** global rescue with fixed relative gap must pay a diverging condition-number cost. The present result handles the maps that condition numbers make vacuous: singular, rectangular, partial-isometric, or pseudoinverse source/target processing. Their corresponding price is a vanishing normalized transmission/covariance scale, with the sharp product law (27).

Thus the global-linear escape is now reduced to a precise analytic obligation. To obtain new coercive information from the full-packed family, one must either (i) prove that the arithmetic supplies enough extra normalization to compensate the forced `O(J sqrt(log p/p))` transmission loss, (ii) change the operator through positive-slack or additional arithmetic data, or (iii) leave the linear full-packed interface. Merely allowing an unrestricted global linear selector no longer constitutes a scale-free escape.