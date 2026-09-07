# ANF-093 — the Lamzouri Schur quotient still has exponential cross-metric blow-up

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + SCHUR-COMPLEMENT + QUOTIENT-CONDITIONING + NEAR-EXTREMAL-SEPARABLE-CONE + CROSS-METRIC-WINDOW-GAP`. `ANF-089` bounds destination distance through a raw source Gram denominator, and `ANF-090`--`ANF-092` show that this raw conditioning can be exponentially bad even on exactly separable Montgomery--Taylor near-extremizers. A natural repair is suggested by the exact projection tax in `ANF-088`: quotient the antisymmetric nonreal modes by Lamzouri's symmetric space `U` first, and only then measure source conditioning. That source-side repair is still insufficient. The resulting Schur-complement Gram can be exponentially more singular than the central-notch real-collapse defect Gram on the **same signed coefficient direction**, even along the exactly separable near-extremizing family of `ANF-092`.

More precisely, for a configuration with simple nonreal conjugate pairs choose one upper representative `z_j=x_j+i y_j`, let

\[
q_j:=(I-P_U)h_{z_j},
\qquad
Q_U(W):=(\langle q_j,q_k\rangle)_{j,k},
\tag{1}
\]

where `U` and `h_z` are the exact Lamzouri objects of `ANF-088`. Let

\[
d_j(\alpha)
:=e^{-2\pi i\alpha z_j}
 +e^{-2\pi i\alpha\bar z_j}
 -2e^{-2\pi i\alpha x_j},
\tag{2}
\]

and let

\[
D_s(W):=(\langle d_j,d_k\rangle_s)_{j,k}
\tag{3}
\]

be the central-notch destination defect Gram of `ANF-089` in the multiplicity-one case. For the configurations used below `Q_U(W)` is positive definite, so define the source-quotiented real-collapse amplification

\[
\boxed{
\Gamma_s(W)
:=
\sup_{c\ne0}
\frac{c^*D_s(W)c}{c^*Q_U(W)c}.
}
\tag{4}
\]

Fix

\[
d:=\frac34,
\qquad
r:=\sin\frac{3\pi}{8}\in(0,1).
\tag{5}
\]

Specialize the exact `ANF-092` sequence to this `d`: its horizontal set contains the dense block

\[
C_n=\{0,d,2d,\ldots,nd\}
\tag{6}
\]

plus the high-zero padding constructed there, and every horizontal center carries the common conjugate fiber `{-y_n,+y_n}` with

\[
y_n=r^{n/8}.
\tag{7}
\]

Write the resulting product multiset as `W_n`. Then `ANF-092` gives

\[
\frac{\Delta(W_n)}{L(W_n)}\longrightarrow0,
\qquad
d_{\rm sep}(W_n)=0.
\tag{8}
\]

Nevertheless there is a constant `C_s>0`, depending only on the fixed central-notch profile, such that for all sufficiently large `n`,

\[
\boxed{
\Gamma_s(W_n)
\ge
\frac{C_s}{2n+1}\,r^{-7n/4}
\longrightarrow\infty.
}
\tag{9}
\]

Thus replacing the raw Gram minimum of `ANF-089` by the **exact Lamzouri Schur quotient** does not cure the conditioning pathology. The failure is not caused by exact redundancy, common pair height, multiplicity, or lack of near-extremality. What remains wrong is the destination comparison: `D_s` still measures collapse to the real axis even though `W_n` itself already lies on the safe all-height separable cone. Any viable quotient-aware stability theorem must therefore quotient or optimize the **destination** against the separable cone as well; source-side Schur residualization alone cannot supply a cardinality-uniform bridge.

## 1. The exact source quotient is a positive Schur-complement Gram

For the two-row product family, every nonreal pair is simple. At a center `x_j` and common height `y>0`, the Lamzouri symmetric and antisymmetric modes are

\[
\begin{aligned}
g_j(u)
&=\eta_{\rm MT}(u)e^{-2\pi iux_j}\cosh(2\pi uy),\\
h_j(u)
&=-i\eta_{\rm MT}(u)e^{-2\pi iux_j}\sinh(2\pi uy),
\end{aligned}
\qquad |u|\le\frac12.
\tag{10}
\]

The space `U` is the span of all `g_j` in the configuration. Therefore `Q_U` in (1) is precisely the Gram matrix of the orthogonal innovations of the antisymmetric block after the complete symmetric block has been removed. In block-Gram language it is the Schur complement of the `g` block.

For the present finite configuration `Q_U` is positive definite. Indeed, if

\[
\sum_j c_j(I-P_U)h_j=0,
\tag{11}
\]

then `sum_j c_j h_j` lies in `U`. Expanding both sides in the distinct complex frequencies `x_j+iy` and `x_j-iy`, an element of `U` has equal coefficients on each conjugate pair, whereas `sum c_j h_j` has opposite coefficients. The finite-exponential independence already used in `ANF-088` therefore forces every `c_j=0`.

So (4) is not exploiting a singular labelled representation. It measures genuine near-dependence **after** the exact source quotient has removed the symmetric space.

## 2. A normalized binomial difference remains exponentially invisible on the source window

On the dense block (6) take the normalized signed coefficient vector

\[
c_{j,n}
:=
\frac{(-1)^j\binom nj}{\sqrt{\binom{2n}{n}}},
\qquad 0\le j\le n,
\tag{12}
\]

and set all padding coefficients to zero. Then

\[
\sum_{j=0}^n|c_{j,n}|^2=1,
\qquad
\sum_{j=0}^nc_{j,n}=0,
\tag{13}
\]

and its exponential synthesis is exactly

\[
P_n(t)
:=\sum_{j=0}^nc_{j,n}e^{-2\pi i djt}
=
\frac{(1-e^{-2\pi i dt})^n}{\sqrt{\binom{2n}{n}}}.
\tag{14}
\]

On Lamzouri's source interval `|u|<=1/2`,

\[
\left|\sin(\pi d u)\right|
\le
\sin\frac{3\pi}{8}
=r.
\tag{15}
\]

Since the central binomial coefficient is the largest of the `2n+1` coefficients summing to `4^n`,

\[
\binom{2n}{n}\ge\frac{4^n}{2n+1}.
\tag{16}
\]

Equations (14)--(16) give the pointwise source-window estimate

\[
\boxed{
|P_n(u)|^2\le(2n+1)r^{2n},
\qquad |u|\le\frac12.
}
\tag{17}
\]

Let `c_n` denote the full coefficient vector obtained by extending (12) by zero on the padding. Using (10), projection contraction, `int eta_MT^2=1`, and `0<y<=1`,

\[
\begin{aligned}
c_n^*Q_U(W)c_n
&=\left\|
(I-P_U)\sum_jc_{j,n}h_j
\right\|_2^2\\
&\le
\int_{-1/2}^{1/2}
\eta_{\rm MT}(u)^2
\sinh^2(2\pi uy)
|P_n(u)|^2\,du\\
&\le
\sinh^2(\pi y)(2n+1)r^{2n}\\
&\le
\boxed{
(\sinh\pi)^2y^2(2n+1)r^{2n}.
}
\end{aligned}
\tag{18}
\]

The final normalization is important. Even after dividing out the trivial small-height factor `y^2`, the Schur-quotient direction is exponentially small. The mechanism is the same short-window finite-difference concentration that made the raw Gram singular in `ANF-090`, but (18) shows that it survives the **actual orthogonal quotient appearing in Lamzouri's projection tax**.

## 3. The same coefficient vector retains fixed normalized mass on the destination window

For a common-height pair, the real-collapse defect (2) is

\[
d_j(\alpha)
=2e^{-2\pi i\alpha x_j}
\bigl(\cosh(2\pi\alpha y)-1\bigr).
\tag{19}
\]

Therefore the same coefficient vector gives

\[
\sum_jc_{j,n}d_j(\alpha)
=2\bigl(\cosh(2\pi\alpha y)-1\bigr)P_n(\alpha).
\tag{20}
\]

The longer destination interval sees a completely different amount of the finite-difference polynomial. Let

\[
I:=\left[-1,\frac13\right],
\qquad
I_0:=\left[-\frac56,-\frac12\right].
\tag{21}
\]

Because `d=3/4`, the length of `I` is exactly the period `1/d=4/3` of the exponential lattice. Orthogonality over one full period and (13) give the exact identity

\[
\boxed{
\int_I|P_n(\alpha)|^2\,d\alpha
=\frac1d\sum_j|c_{j,n}|^2
=\frac43.
}
\tag{22}
\]

The unique maximum of `|sin(pi d alpha)|` in that period occurs at `alpha=-2/3`, inside `I_0`. On the complement `I\setminus I_0`,

\[
|\sin(\pi d\alpha)|\le r.
\tag{23}
\]

Hence (16) gives

\[
\int_{I\setminus I_0}|P_n(\alpha)|^2\,d\alpha
\le
\frac43(2n+1)r^{2n}.
\tag{24}
\]

The right side is at most `2/3` for every `n>=31`. Thus

\[
\boxed{
\int_{I_0}|P_n(\alpha)|^2\,d\alpha
\ge\frac23,
\qquad n\ge31.
}
\tag{25}
\]

Now let

\[
j_*:=\min_{\alpha\in I_0}J_s(\alpha)>0.
\tag{26}
\]

The strict positivity follows from `J_s>=(1-s)J_MT` and the interior positivity of the exact Montgomery--Taylor spectrum. On `I_0`, `|alpha|>=1/2`, and

\[
2(\cosh(2\pi\alpha y)-1)
\ge(2\pi\alpha y)^2
\ge\pi^2y^2.
\tag{27}
\]

Combining (20), (25)--(27),

\[
\boxed{
 c_n^*D_s(W)c_n
\ge
\frac23\,j_*\pi^4y^4,
\qquad n\ge31.
}
\tag{28}
\]

Thus the destination defect loses only the natural `y^4` pair-collapse factor while the source Schur residual loses the additional exponential factor `r^{2n}`.

## 4. The Schur-quotiented amplification diverges inside the near-extremal safe cone

Divide (28) by (18). For every `0<y<=1` and `n>=31`,

\[
\Gamma_s(W)
\ge
\frac{2j_*\pi^4}{3(\sinh\pi)^2}
\frac{y^2}{(2n+1)r^{2n}}
\tag{29}
\]

whenever the configuration contains the dense two-row block and the remaining centers only enlarge `U`. Enlarging `U` can only decrease the denominator in (18), so the high-zero padding of `ANF-092` does not weaken the estimate.

For its exact choice `y=y_n=r^{n/8}`,

\[
y_n^2=r^{n/4}.
\tag{30}
\]

Substitution into (29) proves

\[
\boxed{
\Gamma_s(W_n)
\ge
C_s\frac{r^{-7n/4}}{2n+1},
\qquad
C_s:=\frac{2j_*\pi^4}{3(\sinh\pi)^2}>0,
}
\tag{31}
\]

which is (9).

By `ANF-092`, these same `W_n` are exactly product/separable and satisfy `Delta(W_n)/L(W_n)->0`. Therefore the exponential divergence survives all three repairs that were plausible after `ANF-090`: restrict to the Montgomery--Taylor near-extremizer regime, remove positive-density crowding by dilution, and replace the raw labelled source Gram by the exact Lamzouri orthogonal quotient.

The zero-sum identity in (13) is a useful stress check: the witness is not the uniform coefficient direction across the dense block. It is a high-order signed oscillation. The coefficients are used only as a Rayleigh/generalized-eigenvalue probe; they are **not** themselves multiset occupancies.

## 5. What this rules out, and what it does not

The result rules out a specific next proof architecture. One cannot hope to close the `ANF-086` frontier by saying that the bad raw Gram directions of `ANF-090` disappear after projecting the `h_z` modes away from Lamzouri's symmetric space `U`, and then comparing that Schur residual directly with the real-collapse destination defects of `ANF-089`. Equation (31) shows an exponential mismatch on the exact safe cone.

This does **not** construct a central-notch counterexample. In fact `d_sep(W_n)=0` identically, because the entire family is already separable. The reason `D_s` stays large is precisely that it compares `W_n` with its real-axis collapse instead of with the best separable carrier, which here is `W_n` itself. Nor does (31) show that a fully separable-quotiented generalized singular value diverges: the destination side has deliberately not yet been projected or minimized over the nonlinear product cone.

That distinction sharpens the live gate. The next useful invariant must remove safe directions on **both** sides of the comparison. Concretely, one needs either a direct estimate from the exact projection taxes of `ANF-088` to `d_sep(W)` that never singles out the real collapse, or a genuinely two-sided quotient in which the destination defect is first minimized/projected against the tangent or secant geometry of `Sep(W)`. A source-only Schur complement, however intrinsic on the Lamzouri side, is not enough.

There is also a normalization lesson. `ANF-092` shows that sparse source pathologies can be diluted into global near-extremizers. The present result shows that orthogonal source residualization does not remove their cross-window amplification. Any successful rigidity theorem must therefore retain the **mass localization and destination normalization** built into `d_sep`, rather than infer geometry from an absolute source condition number.

## 6. Prior-art boundary and audit

Schur complements as orthogonal residual Grams are classical. A targeted literature check also found recent quotient/Riesz formulations of the same general principle, notably Matthew Francis Dixon's 2026 preprint *Successive Schur--Riesz Analysis for Approximation* (`arXiv:2608.10757`), and the mature nonharmonic-Fourier/super-resolution literature on exponentially small finite-section singular values, including Batenkov--Goldman's 2021 single-exponential bounds for sub-Rayleigh Vandermonde systems. These sources confirm that quotienting exact redundancy and finite-window exponential conditioning are standard neighboring mechanisms.

No external theorem is used in (10)--(31): the Schur interpretation is the projection identity already internal to `ANF-088`, while the exponential estimate and destination lower bound are the explicit binomial calculation above. The literature audit located no statement coupling Lamzouri's exact `U`-quotient to the central-notch pair-collapse Gram, nor the Mathia-specific conclusion that this source-quotiented cross-metric amplification diverges on an exactly separable Montgomery--Taylor near-extremizing sequence. No new external dependency is therefore load-bearing, and `SOURCES.md` is unchanged.

The durable consequence is narrower than a global no-go but stronger than the raw-conditioning examples before it: **even the exact source quotient identified by the Montgomery--Taylor equality proof is not the missing intrinsic stability invariant. The remaining quotient must be destination-aware and separable-aware.**