# WI-380 — Gamma-negative source-zero modes localize favorable arithmetic repair to critical shifts

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-OPERATOR-AUDIT + SOURCE-CONDITIONED-TRANSLATION-LOCALIZATION + DECISIVE-ROUTE-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-379 left a restricted spectral question: can the signed sum of the exact inherited arithmetic translations repair the fixed-depth gamma-negative band that survives the true source-zero constraints? There is a sharp geometric restriction on how such repair can occur.

Let

\[
A_k=\log(k+1),
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\]

and let `\mathcal A_{A_k}` and the source set `S_k` be those of WI-377. For every fixed depth

\[
0\le \eta<C_\Gamma
\]

there is a finite constant `L_\eta>0`, depending only on `\eta`, such that for all sufficiently large `k` there is a real nonzero source-zero vector `F_k` with

\[
F_k=0\quad\text{a.e. on }S_k,
\qquad
\operatorname{supp}F_k
\subseteq
I_k:=
\left[
\frac{A_k-L_\eta}{2},
\frac{A_k+L_\eta}{2}
\right],
\tag{1}
\]

\[
F_k\ge0,
\qquad
\boxed{
\mathcal A_{A_k}[F_k]\le-\eta\|F_k\|_2^2.
}
\tag{2}
\]

Oddly extend `F_k` to `(-A_k,A_k)` by

\[
f_k(x)=
\begin{cases}
F_k(x),&x>0,\\
-F_k(-x),&x<0.
\end{cases}
\tag{3}
\]

For the physical autocorrelation

\[
C_k(h):=
\int_{\mathbb R}f_k(x+h)f_k(x)\,dx,
\qquad h>0,
\tag{4}
\]

one then has the exact sign/support pattern, once `A_k>2L_\eta`,

\[
\boxed{
\begin{array}{c|c}
0<h<L_\eta & C_k(h)\ge0\\
L_\eta\le h<A_k-L_\eta & C_k(h)=0\\
A_k-L_\eta\le h\le A_k+L_\eta & C_k(h)\le0\\
h>A_k+L_\eta & C_k(h)=0.
\end{array}
}
\tag{5}
\]

Marco Desogus's exact localized odd operator contains the arithmetic branches

\[
-\sum_{2\le n<e^{2A_k}}
\frac{\Lambda(n)}{\sqrt n}
\bigl(S_{\log n/A_k}+S_{\log n/A_k}^*\bigr).
\tag{6}
\]

On a real vector, the branch with physical shift `h=\log n` contributes, up to the fixed unitary normalization between physical and normalized coordinates,

\[
-2\frac{\Lambda(n)}{\sqrt n}C_k(\log n).
\tag{7}
\]

Therefore every arithmetic branch outside the fixed-factor annulus

\[
\boxed{
(k+1)e^{-L_\eta}
\le n\le
(k+1)e^{L_\eta}
}
\tag{8}
\]

is either unfavorable or exactly invisible on this certified depth-`\eta` source-zero trial. More precisely, `\log n<L_\eta` gives a nonpositive arithmetic contribution, `L_\eta\le\log n<A_k-L_\eta` and `\log n>A_k+L_\eta` give zero, and only

\[
|\log n-A_k|\le L_\eta
\tag{9}
\]

can give positive repair.

Equivalently, in Desogus's normalized translation coordinate

\[
r_{n,k}=\frac{\log n}{A_k},
\]

all favorable arithmetic credit on these fixed-depth gamma-negative source-zero modes is forced into

\[
\boxed{
|r_{n,k}-1|\le\frac{L_\eta}{A_k}\longrightarrow0.
}
\tag{10}
\]

Thus the spectral question left by WI-379 cannot be settled in the favorable direction by a small-shift, translation-stationary, Laurent/Toeplitz bulk symbol, by any fixed finite family of prime-power shifts, or by a coercivity estimate supported a fixed normalized distance away from `r=1`. A successful direct arithmetic repair must exploit the **cross-origin critical-shift layer** `r=1+o(1)`, or the admissible category must exclude these source-zero trials before the old--old form is evaluated.

This is a route restriction, not a proof that the full arithmetic sum fails. The critical annulus in (8) contains many prime powers and its positive cross-lobe contribution is not bounded here.

## 1. A fixed-width centered mode reaches every fixed gamma depth

WI-369 gives in physical logarithmic coordinates

\[
\mathcal A_A[F]+C_\Gamma\|F\|_2^2
=D_A[F]+E_A[F]+J_A[F],
\tag{11}
\]

where all three terms on the right are nonnegative, and WI-377 records the whole-line symbol bound

\[
D_A[G]
\le\widetilde D[G]
\le
 d\!\left(\frac{\|G'\|_2}{\|G\|_2}\right)\|G\|_2^2,
\tag{12}
\]

with

\[
d(q)=2\int_0^\infty
\frac{e^{-s/2}}{1-e^{-2s}}(1-\cos qs)\,ds,
\qquad
m(q)=d(q)-C_\Gamma.
\tag{13}
\]

For `0\le\eta<C_\Gamma`, let `q_\eta>0` be the unique solution

\[
m(q_\eta)=-\eta.
\tag{14}
\]

Choose once and for all

\[
L_\eta>\frac\pi{q_\eta}.
\tag{15}
\]

On the centered interval `I_k` in (1), let `G_k` be the normalized first Dirichlet sine mode. Then `G_k\ge0` and

\[
\frac{\|G_k'\|_2}{\|G_k\|_2}
=\frac\pi{L_\eta}<q_\eta,
\]

so strict monotonicity of `d` gives a fixed margin `\mu_\eta>0` such that

\[
-C_\Gamma+d\!\left(\frac\pi{L_\eta}\right)
\le-\eta-\mu_\eta.
\tag{16}
\]

The only issue is enforcing the exact Desogus source zeros without losing this fixed margin.

## 2. Source perforation has vanishing capacity even on the shrinking normalized window

Every source slot in WI-377 has width

\[
\varepsilon_k
=\log\!\left(1+\frac1k\right)
\le\frac1k.
\tag{17}
\]

If a source slot

\[
J_{k,n}
=[\log k-\log n,\,\log(k+1)-\log n)
\]

meets `I_k`, then its right endpoint exceeds `(A_k-L_\eta)/2`, hence

\[
\log n<\frac{A_k+L_\eta}{2}.
\tag{18}
\]

A crude count by all integers therefore gives at most

\[
M_k
\le
\exp\!\left(\frac{A_k+L_\eta}{2}\right)
\tag{19}
\]

relevant slots. Consequently

\[
|S_k\cap I_k|
=O\!\left(e^{-(A_k-L_\eta)/2}\right)
=o(1).
\tag{20}
\]

More importantly, the screened jump cost used in WI-377 also vanishes. A cutoff across one interval of length `O(\varepsilon_k)` costs

\[
O\!\left(\int_0^{C\varepsilon_k}H(x)\,dx\right)
=O(A_k e^{-A_k}),
\tag{21}
\]

because `H(x)=O(1+|\log x|)` at zero. Summing (21) over (19) gives

\[
\boxed{
\kappa_k
=O\!\left(
A_k e^{-(A_k-L_\eta)/2}
\right)
=o(1).
}
\tag{22}
\]

Use the same nonnegative source-slot cutoff construction as WI-377, now restricted to `I_k`, and put

\[
F_k=\chi_kG_k.
\tag{23}
\]

Then `0\le F_k\le G_k`, `F_k=0` on `S_k`, and the fixed-width first-mode bound `\|G_k\|_\infty^2\le2\|G_k\|_2^2/L_\eta`, together with (20)--(22), gives

\[
\|F_k\|_2^2=(1-o(1))\|G_k\|_2^2,
\tag{24}
\]

\[
\frac{D_{A_k}[F_k]}{\|F_k\|_2^2}
\le
 d\!\left(\frac\pi{L_\eta}\right)+o(1).
\tag{25}
\]

Both endpoints are at distance `(A_k-L_\eta)/2` from `I_k`. The endpoint and Hankel estimates of WI-377 specialize to

\[
\frac{E_{A_k}[F_k]+J_{A_k}[F_k]}{\|F_k\|_2^2}
\le
2H\!\left(\frac{A_k-L_\eta}{2}\right)
+L_\eta h(A_k-L_\eta)
=o(1).
\tag{26}
\]

Combining (11), (16), (25), and (26) proves (2) for all sufficiently large `k`. Thus the source-zero negative band contains, at every fixed depth, a particularly rigid representative whose positive-half mass lives in a physical window of **fixed width** centered at `A_k/2`.

## 3. Odd support geometry gives the exact arithmetic sign table

Write

\[
a_k=\frac{A_k-L_\eta}{2},
\qquad
b_k=\frac{A_k+L_\eta}{2}.
\tag{27}
\]

The odd extension in (3) is nonnegative on `[a_k,b_k]`, nonpositive on `[-b_k,-a_k]`, and zero elsewhere. Its two lobes each have diameter `L_\eta`; their nearest points are separated by

\[
2a_k=A_k-L_\eta,
\tag{28}
\]

and their farthest points by

\[
2b_k=A_k+L_\eta.
\tag{29}
\]

For `0<h<L_\eta`, a translate can overlap a lobe only with itself. Every nonzero product in (4) is therefore same-sign and `C_k(h)\ge0`. For

\[
L_\eta\le h<A_k-L_\eta
\]

neither same-lobe nor cross-lobe overlap is possible, so `C_k(h)=0`. For

\[
A_k-L_\eta\le h\le A_k+L_\eta,
\]

same-lobe overlap is impossible while any overlap is from the negative lobe to the positive lobe, so `C_k(h)\le0`. Beyond `A_k+L_\eta` there is no overlap at all. This proves (5) without an estimate: it is pure support and sign geometry and is unchanged by the source holes inside either lobe.

For Desogus's zero-extension translation, real-valuedness gives

\[
\langle f_k,(S_h+S_h^*)f_k\rangle
=2C_k(h),
\tag{30}
\]

in physical coordinates. Since the arithmetic coefficient in (6) is negative, (5) immediately yields the branch-by-branch sign classification claimed after (7).

Two consequences are worth separating. First, every **fixed** prime-power branch is eventually either unfavorable (`\log n<L_\eta`) or invisible (`\log n\ge L_\eta` but `\log n<A_k-L_\eta`); no finite set of fixed translations can pay a positive fixed-depth gamma tariff on these trials. Second, even a growing family of translations whose normalized shifts stay in a compact subset of `(0,1)\cup(1,2)` away from `1` gives no positive credit. The only potentially repairing branches satisfy (10).

## 4. Prior art, novelty boundary, and falsification

The arithmetic operator (6), its coefficient sign, and its zero-extension interpretation are taken only from Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 September 2026), especially the exact normalized localized form and the translation identity in Gate II. The preprint's claimed positivity/RH conclusion is not imported as evidence.

The support facts behind (5) are elementary autocorrelation geometry. General support-of-convolution results such as Titchmarsh's convolution theorem are classical, but no such theorem is needed here: the exact sign follows directly from the two separated one-signed lobes. A targeted search around localized Weil forms, odd compact-support autocorrelations, prime-power translations, and truncated-translation/Toeplitz operators did not locate this fixed-depth source-zero localization statement. Search absence is not evidence of priority, and no priority claim is made.

A July 2026 public working note by Kuberwastaken, *Certified positivity of truncated Weil functionals in low support windows*, reports the numerical phenomenon it calls **just-in-time rescue**: a truncated prime sum becomes indefinite near a prime threshold and the next prime term restores positivity in its finite-dimensional experiments. That observation is qualitatively consistent with a boundary-local arithmetic mechanism, but it is not the result here. It is numerical, is not the Desogus source-zero gamma band, and does not prove the exact localization (8)--(10). Its relevant note is `https://github.com/Kuberwastaken/riemann/blob/main/experiments/weil_positivity/NOTE.md`.

The present finding would fail if the corrected admissible category used before evaluating the old--old arithmetic form excludes the centered source-zero vectors constructed above, if the source-zero slots in WI-377 are not the relevant kernel of the source map for that category, or if the exact arithmetic term on those vectors is not the zero-extension translation sum (6). It also deliberately leaves the critical annulus untreated: (5) makes its sign favorable, not small. Because its Mangoldt-weighted mass can be large, no contradiction with full positivity follows.

## Research consequence

WI-379 showed that inherited arithmetic has enough rank that source-dimension counting cannot kill it. WI-380 shows that **rank is available in the wrong places unless the translation is critical-scale**: on a certified source-zero gamma-negative mode of any fixed depth, every favorable arithmetic branch is squeezed into `r_{n,k}=1+O(1/A_k)`.

The next efficient audit is therefore not a stationary translation symbol near `r=0` and not another ambient-rank argument. It is the cross-origin critical layer

\[
\log n=A_k+O_\eta(1),
\qquad
n\asymp_\eta k,
\tag{31}
\]

with the exact source/domain geometry retained. A proof that this annular contribution cannot meet the WI-378 tariff would close the direct arithmetic repair route on these modes. Conversely, if the claimed rooted induction is correct, this finding identifies where its positive old--old arithmetic energy must actually be concentrated. Either outcome is more specific than the unrestricted signed-sum question left by WI-379.
