# AF-432 — Supercritical packet-center amplitudes are residual but metrically thin

## Status

`EXACT-DERIVED` · `LITERATURE-AUDITED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `SUPERCRITICAL` · `METRIC-DIOPHANTINE` · `BAIRE-CATEGORY` · `SHRINKING-TARGET` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-429--AF-431 on an exact constant rational derivative density

\[
q=\frac uv>2,
\qquad (u,v)=1,
\qquad
\alpha:=1-\frac2q\in(0,1),
\]

with source progression

\[
\mathcal N_q=\{n=vk:k\ge1\},
\qquad
s=qn.
\]

When `v` is odd, the same statements below hold on the odd sign-alternating subprogression

\[
\mathcal N_q^{\mathrm{odd}}
=\{v(2k+1):k\ge0\}.
\]

Fix either of these progressions and denote it by `\mathcal A`. For `a>0`, put

\[
R_n(a)=a^{1/q}n^\alpha,
\]

let `\tau_n(a)` be AF-431's real zero of the exact adjacent full-column log-ratio, and define the first packet-corrected center suggested by AF-430,

\[
\boxed{
\widehat\tau_n(a)
=
\tau_n(a)+a e^q\frac{R_n(a)}{n^2}.
}
\tag{1}
\]

Define the fine-hit amplitude set

\[
\mathcal E_q(\mathcal A)
=
\left\{
a>0:
\begin{array}{l}
\text{there exist }n_j\in\mathcal A,\ n_j\to\infty,\text{ such that}\\[2mm]
\operatorname{dist}\!\left(\widehat\tau_{n_j}(a),\mathbb Z\right)
=
o\!\left(\frac{R_{n_j}(a)}{n_j^2}\right)
\end{array}
\right\}.
\tag{2}
\]

Then

\[
\boxed{
\mathcal E_q(\mathcal A)
\text{ is a dense }G_\delta\text{ subset of }(0,\infty),
}
\tag{3}
\]

while simultaneously

\[
\boxed{
\operatorname{Leb}\bigl(\mathcal E_q(\mathcal A)\bigr)=0,
\qquad
\dim_{\mathrm H}\mathcal E_q(\mathcal A)
\le
1-\frac1q.
}
\tag{4}
\]

Thus the factor-`n` refinement left open by AF-431 has the same qualitative split already seen in AF-427--AF-428, but at a different quantitative scale: the first packet-corrected target is **topologically generic in the amplitude and metrically exceptional**.

Moreover, let `\mathcal B_q(\mathcal A)` denote amplitudes for which there exist `n_j\in\mathcal A` and integers `r_j` in AF-429's first saddle window such that the two complete exceptional-`1` packets satisfy

\[
\log Q_{n_j,r_j}(a)=o(n_j^{-1}).
\tag{5}
\]

AF-430 implies

\[
\boxed{
\mathcal B_q(\mathcal A)\subseteq\mathcal E_q(\mathcal A).
}
\tag{6}
\]

Hence first-order complete-packet balance on this constant-density source class is possible only on a Lebesgue-null amplitude set of Hausdorff dimension at most `1-1/q`. The residuality in `(3)` prevents this metric statement from deciding any fixed distinguished arithmetic amplitude.

## 1. The refined center is transverse in amplitude

For fixed `q`, AF-431 writes the exact real adjacent-ratio equation as

\[
\Phi(n,r;a)
=
qn\log\!\left(
\frac{R_n(a)(n+r)}{nr}
\right)
+E(n,r),
\tag{7}
\]

where `E(n,r)` is independent of `a`, and `\tau_n(a)` is the unique large zero of `r\mapsto\Phi(n,r;a)` near `R_n(a)`.

Because

\[
\frac{\partial_a R_n(a)}{R_n(a)}
=
\frac1{qa},
\]

one has the exact identity

\[
\boxed{
\partial_a\Phi(n,r;a)=\frac n a.
}
\tag{8}
\]

AF-429--AF-431 give, uniformly when `a` ranges over a fixed compact interval `K\Subset(0,\infty)`, 

\[
\tau_n(a)\sim R_n(a),
\qquad
\partial_r\Phi(n,\tau_n(a);a)
=
-q\frac n{R_n(a)}(1+o_K(1)).
\tag{9}
\]

The implicit-function theorem and `(8)`--`(9)` therefore give

\[
\boxed{
\partial_a\tau_n(a)
=
\frac{R_n(a)}{qa}(1+o_K(1)).
}
\tag{10}
\]

The explicit packet displacement in `(1)` is smaller by `n^{-2}`. Indeed,

\[
\partial_a\!\left(
a e^q\frac{R_n(a)}{n^2}
\right)
=
e^q\left(1+\frac1q\right)\frac{R_n(a)}{n^2}.
\tag{11}
\]

Consequently

\[
\boxed{
\partial_a\widehat\tau_n(a)
=
\frac{R_n(a)}{qa}(1+o_K(1)).
}
\tag{12}
\]

Since `R_n(a)=a^{1/q}n^\alpha`, there are constants `0<c_K<C_K<\infty` such that for all sufficiently large admissible `n`,

\[
\boxed{
c_K n^\alpha
\le
\partial_a\widehat\tau_n(a)
\le
C_K n^\alpha
\qquad(a\in K).
}
\tag{13}
\]

Thus the refined center is eventually strictly increasing in the amplitude, and a fixed amplitude interval is expanded to a real saddle interval of length `\Theta_K(n^\alpha)`.

This is the load-bearing fidelity fact. The fine target has width `R_n/n^2=\Theta_K(n^{\alpha-2})` in saddle space, but amplitude transversality divides that width by another factor `\Theta_K(n^\alpha)`. Each individual integer target therefore occupies only `O_K(n^{-2})` amplitude width, independently of `q`.

## 2. Metric covering makes refined hits exceptional

Fix a compact amplitude interval `K=[a_0,a_1]\Subset(0,\infty)` and `k\ge1`. At an admissible scale `n`, define

\[
V_{n,k}(K)
=
\left\{
a\in K:
\operatorname{dist}\!\left(\widehat\tau_n(a),\mathbb Z\right)
<
\frac{R_n(a)}{k n^2}
\right\}.
\tag{14}
\]

Uniformly on `K`,

\[
R_n(a)=\Theta_K(n^\alpha),
\qquad
\widehat\tau_n(a)=\Theta_K(n^\alpha).
\tag{15}
\]

Hence only `O_K(n^\alpha)` integer levels can meet the image `\widehat\tau_n(K)`.

For one such integer `r`, the relevant saddle-space tolerance is at most `C_K n^{\alpha-2}/k`. By the lower derivative bound in `(13)`, the preimage in amplitude space is an interval of length at most

\[
\boxed{
|I_{n,r,k}|
\le
\frac{C_K}{k n^2}.
}
\tag{16}
\]

Therefore

\[
\operatorname{Leb}V_{n,k}(K)
\ll_{K,k}
n^\alpha n^{-2}
=
n^{\alpha-2}.
\tag{17}
\]

Because `\alpha<1`,

\[
\sum_{\substack{n\in\mathcal A\\n\ge1}}
n^{\alpha-2}<\infty.
\tag{18}
\]

The convergence half of the elementary limsup/Borel--Cantelli covering argument gives zero Lebesgue measure to amplitudes lying in infinitely many `V_{n,k}(K)`. Since every amplitude satisfying `(2)` lies in infinitely many such sets for every fixed `k`, one obtains

\[
\operatorname{Leb}\bigl(\mathcal E_q(\mathcal A)\cap K\bigr)=0.
\tag{19}
\]

A countable exhaustion of `(0,\infty)` by compact intervals proves the first part of `(4)`.

The same cover gives a Hausdorff-dimension bound. For `s>0`,

\[
\sum_{\substack{n\in\mathcal A\\n\ge1}}
\sum_r |I_{n,r,k}|^s
\ll_{K,k,s}
\sum_n n^{\alpha-2s}.
\tag{20}
\]

This converges when

\[
\alpha-2s<-1,
\qquad\text{i.e.}\qquad
s>\frac{1+\alpha}{2}
=
1-\frac1q.
\tag{21}
\]

Thus

\[
\dim_{\mathrm H}
\bigl(\mathcal E_q(\mathcal A)\cap K\bigr)
\le
1-\frac1q,
\]

and the compact exhaustion gives the global dimension bound in `(4)`.

No independence, equidistribution, or random-phase assumption enters this estimate. It is a deterministic consequence of the exact source count, the packet target width, and the amplitude derivative of the real saddle.

## 3. Exact roots are dense, so the same set is residual

For integers `k,N\ge1`, let

\[
U_{k,N}
=
\bigcup_{\substack{n\in\mathcal A\\n\ge N}}
\left\{
a>0:
\operatorname{dist}\!\left(\widehat\tau_n(a),\mathbb Z\right)
<
\frac{R_n(a)}{k n^2}
\right\}.
\tag{22}
\]

Every `U_{k,N}` is open by continuity.

To prove density, take a nonempty open amplitude interval `J` and choose a compact nondegenerate subinterval `K\Subset J`. By `(13)`,

\[
|\widehat\tau_n(K)|
\ge
c_K |K| n^\alpha
\longrightarrow\infty
\tag{23}
\]

along either admissible progression. For every sufficiently large admissible `n`, the interval `\widehat\tau_n(K)` therefore has length greater than one and contains an integer `r`. Since `\widehat\tau_n` is continuous and strictly increasing on `K`, there is an `a_n\in K` with

\[
\widehat\tau_n(a_n)=r.
\tag{24}
\]

This exact root belongs to `U_{k,N}` for all sufficiently large `n\ge N`. Hence every `U_{k,N}` is dense.

Finally,

\[
\boxed{
\mathcal E_q(\mathcal A)
=
\bigcap_{k=1}^\infty
\bigcap_{N=1}^\infty
U_{k,N}.
}
\tag{25}
\]

The forward inclusion follows from the `o(R_n/n^2)` condition. Conversely, choose successively from `U_{j,N_j}` with `N_j` larger than the previously chosen source index; this produces a subsequence on which the normalized distance is below `1/j`.

Equation `(25)` and the Baire category theorem prove `(3)`.

The conclusion is therefore genuinely pointwise-sensitive: every amplitude neighborhood contains exact refined-center hits at arbitrarily large source scales, while almost every fixed amplitude belongs to only finitely many target windows of any fixed normalized size.

## 4. Consequence for complete packet balance

For exact constant density `q`, AF-430 gives in the AF-429 first window

\[
\log Q_{n,r}
=
\Phi_n(r)
+\frac{q a e^q}{n}
+o(n^{-1}),
\tag{26}
\]

and its local saddle slope is

\[
\Phi_n(r)
=
-q\frac n{R_n}(r-\tau_n)(1+o(1)).
\tag{27}
\]

Therefore the stronger packet-balance condition

\[
\log Q_{n,r}=o(n^{-1})
\]

forces

\[
r-\tau_n
=
a e^q\frac{R_n}{n^2}
+
o\!\left(\frac{R_n}{n^2}\right),
\tag{28}
\]

which is exactly the membership condition `(2)` for the leading corrected center `(1)`. This proves `(6)`.

This is only a necessary condition. AF-430 controls the first relative drift of the complete residual packets inside the exceptional-`1` sector; it does not provide a uniform next-order expansion strong enough to reverse `(6)`, and it does not control the omitted-`1` or singular-block determinant sectors. In particular, an exact root of `\widehat\tau_n(a)-r` is not by itself a proof of cancellation in the full determinant.

For `v` odd, applying the theorem on `\mathcal N_q^{\mathrm{odd}}` keeps the sign alternation needed for adjacent packet cancellation. When `v` is even, the exact constant-density progression contains only even `n`; the metric/category theorem still classifies the refined integer target, but it does not create an alternating-sign cancellation mechanism.

## Prior-art and novelty audit

Fractional parts of sublinear power sequences are classical objects of uniform-distribution and metric Diophantine theory. Niclas Technau and Nadav Yesha, **“On the correlations of `n^alpha` mod 1,”** *Journal of the European Mathematical Society* 25 (2023), no. 10, 4123–4154, DOI `10.4171/JEMS/1281`, recalls the Fejér--Csillag theorem that `{n^beta}` is uniformly distributed modulo one for every positive nonintegral `beta` and studies much finer local statistics. This places the bare power-law modulo-one aspect of the present source mesh firmly in established prior art.

Limsup-set measure and Hausdorff-dimension methods are likewise classical. Victor Beresnevich, Detta Dickinson, and Sanju Velani, **“Measure theoretic laws for lim sup sets,”** *Memoirs of the American Mathematical Society* 179 (2006), no. 846, DOI `10.1090/MEMO/0846`, develops a broad metric-Diophantine framework for measure and Hausdorff laws of limsup sets. John C. Oxtoby, ***Measure and Category: A Survey of the Analogies between Topological and Measure Spaces***, 2nd ed., Graduate Texts in Mathematics 2, Springer (1980), DOI `10.1007/978-1-4684-9339-9`, is a classical source for Baire-category existence methods and the measure/category contrast.

No novelty is claimed for Baire's theorem, Borel--Cantelli, elementary Hausdorff covering bounds, shrinking-target language, or uniform distribution of power sequences. The proof above does not require equidistribution, ubiquity, or correlation theorems.

The durable Mathia specialization is the exact source-interface calculation: AF-429--AF-431 identify the supercritical saddle, AF-430 fixes the first packet displacement, and differentiation of that exact saddle with respect to the physical amplitude makes each `R_n/n^2` integer target only `O(n^{-2})` wide in amplitude. This yields the explicit bound `dim_H <= 1-1/q` and shows that the first packet-corrected source gate is simultaneously residual and metric-exceptional.

## Boundaries and falsification checks

- The theorem fixes a rational constant density `q=u/v>2`. It does not classify arbitrary varying sequences `q_n->sigma`.
- The set `\mathcal E_q` is defined by AF-430's **first displayed packet correction**. Higher packet corrections may move the true balance center on a smaller scale, so membership in `\mathcal E_q` is necessary but not sufficient for actual packet cancellation.
- The measure and dimension conclusions concern variation of the amplitude `a`. They make no membership statement for any particular distinguished arithmetic amplitude.
- Residuality does not contradict Lebesgue-nullness or the Hausdorff upper bound; measure and Baire category are independent notions of genericity.
- The dimension bound is an upper bound only. No lower bound or exact dimension is proved.
- For the odd sign-alternating application one needs `v` odd and the odd progression `n=v(2k+1)`. The even-denominator constant-density progression does not supply this sign pattern.
- The complete-packet implication `(6)` remains inside AF-430's exceptional-`1` Cauchy--Binet sector. The omitted-`1` and singular-block determinant sectors are not controlled.
- No rational-prime discriminator, zeta-zero recovery, or implication for RH is established.

## Consequence for the research line

AF-431 showed that the first supercritical `R_n/n` source window is automatic for every amplitude on an exact rational constant-density source lattice. AF-432 now classifies the next factor-`n` refinement: the `R_n/n^2` packet-corrected target is dense and residual as an amplitude property, but only a Lebesgue-null, Hausdorff-thin set of amplitudes can hit it infinitely often.

Therefore neither “the source mesh is too coarse” nor “fine hits are generic” is an adequate pointwise conclusion. The next decisive question for a concrete source-forced amplitude is arithmetic membership in `\mathcal E_q`, exactly as the critical branch required pointwise membership after AF-427--AF-428. Generic measure and category arguments have now exhausted their discriminating power at this first corrected supercritical scale.

If a distinguished amplitude is proved to lie in `\mathcal E_q`, the next analysis must derive the subsequent uniform packet correction and compare omitted determinant sectors. If it is excluded by an arithmetic lower bound, the constant-rational supercritical cancellation route closes at the first packet-corrected source gate.
