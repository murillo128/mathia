# ANF-087 — Montgomery--Taylor equality is a two-site real zero-set packing

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SHARP-EQUALITY + QUANTITATIVE-DEFICIT + ZERO-SET-SUM-FREE + STATIONARY-PALM-CLOSURE`. `ANF-002` imports Lamzouri's conjugation-invariant Hilbert inequality for the Montgomery--Taylor kernel, `ANF-030` identifies the explicit sharp kernel and shows that any stationary/Palm witness at the exact Montgomery--Taylor diffraction budget must place all off-diagonal pair mass on its real zero set, and `ANF-086` leaves a quantitative near-extremizer-to-separable-cone rigidity problem. Reopening Lamzouri's proof at equality gives a sharper boundary than the inequality alone: the entire excess over the Hilbert floor has an explicit nonnegative deficit decomposition. Exact equality excludes every nonreal point. For the explicit Montgomery--Taylor extremizer, its positive real zero set is moreover sum-free, so an equality configuration has at most two distinct support sites.

Let

\[
\theta:=2^{-1/2},
\qquad
 g(u):=\frac{\cos(\sqrt2\,u)}{\sqrt2\sin\theta}\,
 \mathbf 1_{[-1/2,1/2]}(u),
\qquad
\eta_{\rm MT}:=\sqrt g.
\tag{1}
\]

By `ANF-030`, `g>0` on `(-1/2,1/2)`, `\int g=1`, and

\[
K(x):=\widehat g(x)
=\frac{\cos(\pi x)-\sqrt2\,\pi x\cot\theta\,\sin(\pi x)}
       {1-2\pi^2x^2},
\qquad
F_{\rm MT}(x)=K(x)^2.
\tag{2}
\]

For a nonempty finite conjugation-invariant multiset `W`, write

\[
E_{\rm MT}(W):=\sum_{z,w\in W}F_{\rm MT}(z-w),
\qquad
L(W):=2|W|-\sigma(W),
\tag{3}
\]

where `sigma(W)` is the number of simple real sites. Lamzouri's Proposition 2.1 gives

\[
E_{\rm MT}(W)\ge L(W).
\tag{4}
\]

The exact equality class is

\[
\boxed{
E_{\rm MT}(W)=L(W)
\iff
\begin{cases}
W\subset\mathbb R,\\
\text{every distinct site has multiplicity }1\text{ or }2,\\
K(x-y)=0\text{ for every two distinct support sites }x,y.
\end{cases}}
\tag{5}
\]

For the explicit kernel (2), the last condition can hold for at most two distinct sites. Thus every sharp finite configuration is, up to translation, either a single real site of multiplicity one or two, or two real sites of multiplicities independently in `{1,2}` whose separation is one of the positive zeros of `K`.

## 1. Lamzouri's proof contains an exact nonnegative deficit decomposition

Use Lamzouri's notation from the proof of Proposition 2.1. For each `z in W`, put

\[
f_z(u)=\eta_{\rm MT}(u)e^{-2\pi iuz},
\qquad
g_z=\frac{f_z+f_{\bar z}}2,
\qquad
h_z=\frac{f_z-f_{\bar z}}{2i}.
\tag{6}
\]

Let `R_1` be the distinct simple real sites, `R_2` the distinct real sites of multiplicity at least two, and choose one representative from each nonreal conjugate pair. Write

\[
n:=|R_1|,
\qquad r:=|R_2|,
\qquad k:=\#\{\text{distinct nonreal conjugate pairs}\}.
\tag{7}
\]

Lamzouri introduces the nested subspaces

\[
U\subset V\subset \mathcal W
\tag{8}
\]

where `U` is spanned by the `f_x` for `x in R_2` together with the `g_z` for the nonreal representatives, `V` additionally contains the simple-real `f_x`, and `mathcal W` additionally contains the `h_z`. Let their dimensions be `D_U,D_V,D_W`, and choose an orthonormal basis `psi_1,...,psi_{D_W}` adapted to these inclusions. Set

\[
\Psi_j(u,v):=\psi_j(u)\psi_j(v),
\qquad
\alpha_j:=\langle \mathcal F,\Psi_j\rangle,
\tag{9}
\]

where

\[
\mathcal F(u,v):=\sum_{z\in W}f_z(u)f_z(v).
\tag{10}
\]

Lamzouri proves

\[
E_{\rm MT}(W)=\|\mathcal F\|_2^2,
\qquad
\sum_{j=1}^{D_W}\alpha_j=|W|,
\tag{11}
\]

and the three structural inequalities

\[
A_U:=\sum_{j\le D_U}\alpha_j\ge2D_U,
\qquad
D_V-D_U\le n,
\qquad
\alpha_j\le0\quad(j>D_V).
\tag{12}
\]

Let

\[
\mathcal B
:=\|\mathcal F\|_2^2-
\sum_{j=1}^{D_W}\alpha_j^2\ge0
\tag{13}
\]

be the Bessel residual and put `d:=D_V-D_U`. Subtracting `L(W)=2|W|-n` from (11) and completing squares separately on the three index ranges gives the exact identity

\[
\boxed{
\begin{aligned}
E_{\rm MT}(W)-L(W)
={}&\mathcal B\\
&+\sum_{j\le D_U}(\alpha_j-2)^2
  +2(A_U-2D_U)\\
&+\sum_{D_U<j\le D_V}(\alpha_j-1)^2
  +(n-d)\\
&+\sum_{j>D_V}(\alpha_j^2-2\alpha_j).
\end{aligned}}
\tag{14}
\]

Every term on the right is nonnegative by (12). This is the quantitative form of the Hilbert inequality relevant to the frontier of `ANF-086`. In particular, if the Montgomery--Taylor excess is `Delta`, then the Bessel residual is at most `Delta`, the first-range coefficients are `l^2`-close to `2`, the middle coefficients are `l^2`-close to `1`, and the last-range coefficients have total penalty at most `Delta`. The integer defect satisfies

\[
0\le n-(D_V-D_U)\le\Delta.
\tag{15}
\]

Hence any configuration with `Delta<1` already has `D_V-D_U=n` exactly. This is basis-adapted Hilbert rigidity; it is not yet the geometric `d_sep` estimate demanded by `ANF-086`.

## 2. Equality in the first range rules out every nonreal pair

Suppose now that `E_MT(W)=L(W)`. Equation (14) forces

\[
A_U=2D_U.
\tag{16}
\]

The stronger estimate used inside Lamzouri's proof is

\[
\begin{aligned}
A_U
&=\sum_{x\in R_2}m_x
+2\sum_{z}m_z
\left(\|g_z\|_2^2-\|P_Uh_z\|_2^2\right)\\
&\ge
\sum_{x\in R_2}m_x
+2\sum_zm_z
\left(\|g_z\|_2^2-\|h_z\|_2^2\right)\\
&=\sum_{x\in R_2}m_x+2\sum_zm_z\\
&\ge2(r+k)\ge2D_U.
\end{aligned}
\tag{17}
\]

Here `P_U` is orthogonal projection onto `U`, and Lamzouri's identity

\[
\|g_z\|_2^2-\|h_z\|_2^2=1
\tag{18}
\]

is used. Combining (16)--(17) forces equality at every step. In particular, every repeated real multiplicity is exactly two, every nonreal-pair multiplicity is exactly one, `D_U=r+k`, and

\[
h_z\in U
\tag{19}
\]

for each nonreal representative `z`.

For the Montgomery--Taylor extremizer, (19) is impossible. Indeed `eta_MT>0` on the open interval `(-1/2,1/2)`. After division by `eta_MT`, the functions `f_w` are the exponentials `e^{-2 pi i u w}`. Finite exponentials with distinct complex frequencies are linearly independent on any open real interval: differentiating a putative relation at one interior point gives a Vandermonde system.

But `U` is spanned by real-frequency `f_x` and the symmetric combinations

\[
g_z=\frac{f_z+f_{\bar z}}2,
\tag{20}
\]

whereas

\[
h_z=\frac{f_z-f_{\bar z}}{2i}.
\tag{21}
\]

No linear combination of the generators in (20) and the distinct real-frequency exponentials can produce (21): the unique coefficients of the frequencies `z` and `bar z` would have to be simultaneously equal and opposite. Exponential independence therefore contradicts (19) whenever `k>0`. Hence

\[
\boxed{E_{\rm MT}(W)=L(W)\Longrightarrow W\subset\mathbb R.}
\tag{22}
\]

This is stronger than merely saying that a nonreal configuration has positive Hilbert excess: it identifies the exact equality obstruction inside Lamzouri's own proof.

## 3. The all-real equality class is a zero-set packing with multiplicities at most two

Once `W` is real, write its distinct sites as `x_1,...,x_q` with multiplicities `m_i`. Since `K` is real on the real axis,

\[
E_{\rm MT}(W)
=\sum_i m_i^2
+2\sum_{i<j}m_im_jK(x_i-x_j)^2.
\tag{23}
\]

Every term is nonnegative. On the other hand

\[
L(W)
=\sum_i\left(2m_i-\mathbf 1_{m_i=1}\right).
\tag{24}
\]

The diagonal contributions agree with (24) exactly for `m_i=1` and `m_i=2`; for `m_i>=3` their excess is

\[
m_i^2-2m_i=m_i(m_i-2)>0.
\tag{25}
\]

Consequently equality in (23)--(24) holds exactly when every `m_i` belongs to `{1,2}` and every off-diagonal term vanishes. This proves (5).

The conclusion also supplies the finite-configuration analogue of the Palm support statement in `ANF-030`: sharp Montgomery--Taylor equality has no diffuse or complex degree of freedom. It is a real packing whose difference set is contained in the zero set of the exact extremizer.

## 4. The positive Montgomery--Taylor zero set is sum-free

The remaining zero-set geometry is elementary once the explicit formula (2) is used. Put

\[
a:=\sqrt2\,\pi\cot\theta>0.
\tag{26}
\]

Away from the removable points of (2), a positive zero of `K` satisfies

\[
\tan(\pi x)=\frac1{ax}.
\tag{27}
\]

For every integer `n>=0`, the left side increases from `0` to `+infinity` on `(n,n+1/2)`, while the right side is positive and strictly decreasing. Hence there is exactly one solution there, and there is no solution on `(n+1/2,n+1)` because the tangent is negative.

For `n=0` the unique solution is

\[
x_0=\frac{1}{\sqrt2\pi}=\frac\theta\pi,
\tag{28}
\]

which is exactly the removable zero shared by the numerator and denominator of (2), not a zero of `K`. L'Hopital gives

\[
K(x_0)
=\frac{\csc\theta+\theta^{-1}\cos\theta}{4\theta}>0.
\tag{29}
\]

Therefore the positive zeros of `K` are precisely

\[
r_n=n+\delta_n,
\qquad n=1,2,\ldots,
\qquad 0<\delta_n<\frac12,
\tag{30}
\]

where

\[
\tan(\pi\delta_n)
=\frac1{a(n+\delta_n)}.
\tag{31}
\]

The sequence `delta_n` is strictly decreasing. Indeed, for fixed `delta in (0,1/2)`, the left side of (31) is unchanged while the right side decreases strictly as `n` increases; uniqueness of the crossing then forces `delta_{n+1}<delta_n`.

Now take any two positive zeros `r_m,r_n`. If `delta_m+delta_n>=1/2`, then

\[
r_m+r_n\in[m+n+1/2,m+n+1),
\tag{32}
\]

which contains no positive zero. If `delta_m+delta_n<1/2`, the sum lies in `(m+n,m+n+1/2)`, whose unique zero is `r_{m+n}`. But

\[
\delta_m+\delta_n>\delta_{m+n},
\tag{33}
\]

since already `delta_m>delta_{m+n}` and `delta_n>0`. Hence `r_m+r_n>r_{m+n}`, so the sum again is not a zero. Thus

\[
\boxed{
r_m+r_n\notin Z(K)
\quad\text{for every }m,n\ge1.}
\tag{34}
\]

In particular there do not exist positive `u,v` for which `u`, `v`, and `u+v` are all zeros of `K`. If three distinct real points `x_1<x_2<x_3` had every pairwise difference in `Z(K)`, then

\[
u=x_2-x_1,
\qquad v=x_3-x_2,
\qquad u+v=x_3-x_1
\tag{35}
\]

would contradict (34). Hence every real zero-set packing contains at most two distinct sites, proving the final statement in the headline theorem.

## 5. This closes the stationary/Palm equality route left open in ANF-030

`ANF-030` proves that if a normalized stationary diffraction witness at the sharp Montgomery--Taylor budget has a positive Palm correlation representation

\[
\eta=\delta_0+\eta^\circ,
\qquad \eta^\circ\ge0,
\tag{36}
\]

then

\[
\operatorname{supp}\eta^\circ\subseteq Z(K).
\tag{37}
\]

It left open whether a positive-density stationary/Palm configuration could have all pair differences in that zero set. Equation (34) rules this out much more strongly.

For a genuine stationary point-process realization, (37) and positivity imply that the expected number of ordered pairs whose displacement lies in any compact subset of `R\setminus Z(K)` is zero. A countable exhaustion by bounded rational windows therefore gives, almost surely, no pair with a forbidden displacement. Every realization would have all distinct pair differences in `Z(K)` and hence, by (35), contain at most two points in total.

That is incompatible with positive intensity `lambda`: stationarity gives expected point count `2R lambda` in `[-R,R]`, while a realization containing at most two points has expectation at most two for every `R`. Therefore

\[
\boxed{\text{no positive-intensity stationary point process can realize the sharp Palm support condition of ANF-030.}}
\tag{38}
\]

This closes the stationary-process realization branch at the exact Montgomery--Taylor budget. It does **not** by itself close the larger abstract weak-* convex body of `ANF-020`/`ANF-030`, because a dominated abstract diffraction witness need not come equipped with a realizable positive Palm point process.

## 6. Consequence for the current complex frontier

`ANF-086` shows that a central-notch obstruction must be both Montgomery--Taylor near-extremal and a fixed positive `J_s`-Hilbert distance from every compatible separable carrier. The equality classification above establishes the endpoint of that problem:

\[
E_{\rm MT}(W)=L(W)
\quad\Longrightarrow\quad
W\text{ is real and separable, hence }d_{\rm sep}(W)=0.
\tag{39}
\]

Equation (14) gives more than the endpoint: it identifies the complete Hilbert-space deficit that must be converted into geometric center-height rigidity. The missing step is now precise. One must either prove that small values of the right side of (14) force small `d_sep`, uniformly over growing cardinality and unbounded horizontal geometry, or construct a sequence for which the Lamzouri deficit tends to zero while the destination-norm distance from the separable cone stays bounded below.

No uniform modulus is claimed here. The zero locations satisfy `delta_n downarrow 0`, so large horizontal scales can create increasingly fine approximate additive relations even though exact additive triples are impossible. The present theorem removes exact nonseparable extremizers and closes the stationary/Palm equality realization, but the quantitative near-extremizer problem of `ANF-086` remains the decisive all-cardinality gate.

## 7. Prior art, audit, and evidence boundary

Lamzouri's Proposition 2.1, its nested-space/Bessel proof, and the inequalities used in (11)--(12) are literature inputs already anchored in `SOURCES.md`. The explicit Montgomery--Taylor equality function (2) and its extremal role are classical and already anchored through Carneiro--Chandee--Littmann--Milinovich and `ANF-030`. No novelty is claimed for Bessel's inequality, equality in orthogonal projection, linear independence of finite exponentials, or monotonicity of tangent.

The Mathia-specific derivation is the exact deficit identity (14), the resulting finite-multiset equality classification (5), and the observation that the explicit extremizer's positive zero set is sum-free by the monotone root offsets (30)--(34). A targeted literature search by the explicit extremizer formula, Montgomery--Taylor zero-set language, and additive/sum-free formulations did not locate this classification or the stationary-Palm consequence. Absence of such a hit is not a theorem-level novelty claim.

The load-bearing audit is exact and has four failure points. First, (14) requires Lamzouri's adapted basis and the sign `alpha_j<=0` on the final range; replacing that proof by an arbitrary Bessel decomposition would not suffice. Second, excluding nonreal equality uses the strict interior positivity of the exact Montgomery--Taylor `g`, so division by `eta_MT` is legitimate on an open interval. Third, the solution (28) of the tangent equation is removable and must not be counted as a zero; (29) checks this explicitly. Fourth, the Palm closure (38) is asserted only for an actual positive-intensity stationary point-process realization, not for every abstract positive measure or weak-* diffraction element.

The result does not improve the `0.6725007...` zeta proportion, prove the central-notch inequality for all complex multisets, give a uniform quantitative stability modulus, or imply RH. Its line-level effect is narrower and structural: exact Montgomery--Taylor extremality has no genuinely complex or positive-density stationary realization, and the surviving pairwise-complex frontier is now purely a **near-equality stability** problem rather than an equality-classification problem.