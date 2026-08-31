# WI-060 — the retained `W` spectrum has super-polylogarithmic Wiener norm, so termwise fixed-log twist bounds cannot close

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, improve Mathia's current unconditional simple-critical proportion, or prove that additive twists at growing conductor are individually uncontrollable. It closes a narrower but important assembly route left open by WI-057--WI-059: after retaining enough of the deterministic `W`-local Fourier spectrum to make the discarded `L^2` energy `o(1)`, one cannot combine per-mode estimates carrying only an arbitrary **fixed power of logarithmic saving** by absolute summation. The retained Wiener (`l^1`) mass is already super-polynomial in `log X`, while the corresponding `l^2` mass remains only polylogarithmic.

The durable separation is

\[
\boxed{
\sum_{d(a)\le D_w}|\widehat G_{W,h}(a)|
\ge D_w^{1-o(1)}
\gg_A (\log X)^A
\quad\text{for every fixed }A,
}
\tag{1}
\]

at the sufficient cutoff `D_w` of WI-059, whereas Parseval and WI-058 give

\[
\boxed{
\left(\sum_{d(a)\le D_w}|\widehat G_{W,h}(a)|^2\right)^{1/2}
\le \|G_{W,h}\|_2
\ll \log w.
}
\tag{2}
\]

Thus the next viable analytic interface is intrinsically collective: a weighted square-function/large-sieve estimate, cross-mode orthogonality or cancellation, or a direct theorem for the conditioned covariance. A black-box estimate for each retained additive character followed by triangle inequality is structurally too expensive.

## 1. Input and normalization from WI-058--WI-059

Use the normalized finite Fourier transform and the notation of WI-058:

\[
W=\prod_{p\le w}p,
\qquad
G_{W,h}=\frac{F_{W,h}}{\mathbb E F_{W,h}},
\qquad
\mathbb E G_{W,h}=1,
\tag{3}
\]

and let

\[
d(a)=\frac{W}{(a,W)}
\tag{4}
\]

be the reduced conductor of the character `a mod W`. WI-059 shows that a sufficient cutoff for the **absolute** discarded Fourier `L^2` energy to be `o(1)` is

\[
D_w=w^{K(w)},
\qquad
K(w)=\frac{(2+\eta)\log\log w}{\log\log\log w},
\tag{5}
\]

for any fixed `eta>0`. At the Shao--Teräväinen scale

\[
w=(\log X)^C,
\tag{6}
\]

this becomes

\[
\log D_w
=(2+\eta+o(1))C
\frac{\log\log X\,\log\log\log X}
{\log\log\log\log X}.
\tag{7}
\]

WI-059 also proves that a fixed power `w^K`, equivalently a fixed polylogarithmic conductor in `X`, cannot capture `1-o(1)` of the normalized `L^2` energy. The question here is therefore what it costs to control **all retained modes** up to a cutoff of the genuinely sufficient size (5).

## 2. Exact local Wiener mass

The local normalized factor at an odd prime `p<=w` has mean one. Its nonzero Fourier coefficients can be computed exactly.

If `p|h`,

\[
G_{p,h}(n)=\frac{p}{p-1}\,1_{p\nmid n}.
\tag{8}
\]

For every nonzero frequency `r mod p`, normalized Fourier inversion gives

\[
\widehat G_{p,h}(r)=-\frac1{p-1}.
\tag{9}
\]

Hence the total nonzero local Wiener mass is

\[
\boxed{
L_p(h):=\sum_{r\ne0}|\widehat G_{p,h}(r)|=1.
}
\tag{10}
\]

If `p\nmid h`,

\[
G_{p,h}(n)=\frac{p}{p-2}\,1_{p\nmid n(n+h)}.
\tag{11}
\]

For `r\ne0`, up to the harmless choice of Fourier sign convention,

\[
\widehat G_{p,h}(r)
=-\frac{1+e(rh/p)}{p-2},
\tag{12}
\]

so multiplication by `h` permutes the nonzero residues and

\[
L_p(h)
=\frac{2}{p-2}
\sum_{r=1}^{p-1}\left|\cos\frac{\pi r}{p}\right|.
\tag{13}
\]

For odd `p`, the elementary trigonometric sum is

\[
\sum_{r=1}^{p-1}\left|\cos\frac{\pi r}{p}\right|
=\csc\frac{\pi}{2p}-1,
\tag{14}
\]

and therefore

\[
\boxed{
L_p(h)=
\frac{2\left(\csc(\pi/(2p))-1\right)}{p-2}>1.
}
\tag{15}
\]

Indeed, `L_p>1` is equivalent to `sin(pi/(2p))<2/p`, while

\[
\sin\frac{\pi}{2p}
<\frac{\pi}{2p}
<\frac2p.
\tag{16}
\]

Thus **every odd local prime contributes at least unit nonzero Wiener mass**, whether or not it divides the shift. The prime `2` can simply be omitted from the lower bound; in the locally admissible even-shift regime its treatment is pinned and changes no asymptotic below.

## 3. CRT tensorization makes the low-conductor `l^1` mass combinatorially large

Because `W` is squarefree and `G_{W,h}` is the product of its local factors, the normalized Fourier transform tensorizes under the Chinese remainder theorem. The zero-frequency coefficient of every local factor is one. Therefore, for any set `S` of odd primes `p<=w`, the aggregate absolute Fourier mass of characters whose set of nonzero local frequencies is **exactly** `S` is

\[
\prod_{p\in S}L_p(h)\ge1.
\tag{17}
\]

Let

\[
P:=\pi(w)-1
\tag{18}
\]

be the number of odd primes up to `w`. For an integer `k>=0`, every support set with `|S|<=k` has conductor

\[
d(a)=\prod_{p\in S}p\le w^{|S|}\le w^k.
\tag{19}
\]

Consequently the truncated Wiener norm

\[
A_w(D):=
\sum_{d(a)\le D}|\widehat G_{W,h}(a)|
\tag{20}
\]

obeys the completely deterministic lower bound

\[
\boxed{
A_w(w^K)
\ge
\sum_{j=0}^{\lfloor K\rfloor}\binom Pj
\ge
\binom Pk,
\qquad k:=\lfloor K\rfloor.
}
\tag{21}
\]

For `1<=k<=P`, using the falling-factorial formula and `k!<=k^k`,

\[
\binom Pk
=\frac{P(P-1)\cdots(P-k+1)}{k!}
\ge
\left(\frac{P-k+1}{k}\right)^k.
\tag{22}
\]

Whenever `k=o(P)`, this gives

\[
\boxed{
\log A_w(w^K)
\ge
k\bigl(\log P-\log k+o(1)\bigr).
}
\tag{23}
\]

No cancellation, prime-distribution theorem beyond `P=pi(w)-1`, or probabilistic approximation enters (17)--(23). This is just the exact local Fourier transform plus CRT tensorization.

## 4. At the WI-059 cutoff the Wiener norm beats every fixed power of `log X`

Insert the sufficient exponent from (5):

\[
K(w)=\frac{(2+\eta)\log\log w}{\log\log\log w}.
\tag{24}
\]

Since `P~w/log w`, one has `K=o(P)`, while

\[
\log P=\log w-\log\log w+O(1),
\qquad
\log K=o(\log w).
\tag{25}
\]

Equations (23)--(25) imply

\[
\log A_w(D_w)
\ge
(1-o(1))K(w)\log w
=(1-o(1))\log D_w,
\tag{26}
\]

hence

\[
\boxed{
A_w(D_w)\ge D_w^{1-o(1)}.
}
\tag{27}
\]

Under `w=(log X)^C`, (7) and (26) give the more explicit lower scale

\[
\log A_w(D_w)
\ge
(2+\eta+o(1))C
\frac{\log\log X\,\log\log\log X}
{\log\log\log\log X}.
\tag{28}
\]

For every fixed `A>0`,

\[
\log (\log X)^A=A\log\log X,
\tag{29}
\]

and the ratio of the right side of (28) to (29) is

\[
\frac{(2+\eta)C}{A}
\frac{\log\log\log X}{\log\log\log\log X}
\longrightarrow\infty.
\tag{30}
\]

Therefore

\[
\boxed{
\frac{A_w(D_w)}{(\log X)^A}\longrightarrow\infty
\quad\text{for every fixed }A.
}
\tag{31}
\]

The retained Fourier family is still subpolynomial in `X`, but its **absolute coefficient mass is super-polylogarithmic**.

## 5. Decisive barrier for termwise fixed-log twisted estimates

Suppose, optimistically, that one can prove a source-faithful twisted pair estimate for every retained mode of the form

\[
|S_{d,a}(h)|
\le
Y(\log X)^{-A},
\tag{32}
\]

uniformly for `d<=D_w`, where `A` can be taken arbitrarily large but is fixed independently of `X`. This is stronger than what is presently established for the conditioned Yang covariance, so it is a fair stress test of the naive assembly route.

If the modes are then combined only by triangle inequality, their contribution is bounded by

\[
\begin{aligned}
\sum_{d(a)\le D_w}
|\widehat G_{W,h}(a)|\,|S_{d,a}(h)|
&\le
Y(\log X)^{-A}A_w(D_w).
\end{aligned}
\tag{33}
\]

But (31) says that the coefficient factor on the right dominates **every fixed power** of `log X`. Hence no choice of fixed `A` makes (33) `o(Y)` by this argument. Equivalently,

\[
\boxed{
\text{fixed-log saving per retained mode}
+\text{triangle inequality}
\quad\text{cannot close the WI-059 cutoff.}
}
\tag{34}
\]

This is an assembly no-go, not a theorem that the actual signed sum is large. It leaves open precisely the mechanisms that triangle inequality destroys: cancellation between modes, orthogonality, averaged twist estimates, and direct conditioned covariance estimates.

## 6. The `l^1` obstruction is absent in `l^2`

The contrast with the Hilbert-space norm is sharp. Parseval and WI-058 give

\[
\sum_a|\widehat G_{W,h}(a)|^2
=\|G_{W,h}\|_2^2
\ll(\log w)^2.
\tag{35}
\]

Therefore for the same retained family,

\[
\boxed{
\left(
\sum_{d(a)\le D_w}|\widehat G_{W,h}(a)|^2
\right)^{1/2}
\ll\log w,
}
\tag{36}
\]

whereas its `l^1` mass satisfies (27)--(31). The gap is not cosmetic: it says that any successful mode-by-mode reformulation should preserve an `l^2` or square-function structure rather than expand the local main and immediately take absolute values.

A schematic sufficient interface would look like

\[
\left(
\sum_{d(a)\le D_w}
\omega_{d,a}^{-1}|S_{d,a}(h)|^2
\right)^{1/2}
=o(Y)
\tag{37}
\]

with weights compatible with

\[
\sum_{d(a)\le D_w}
\omega_{d,a}|\widehat G_{W,h}(a)|^2
\ll (\log w)^{O(1)},
\tag{38}
\]

or an equivalent large-sieve/joint-covariance theorem. Equations (37)--(38) are a **target interface**, not a claimed theorem.

## 7. Stress tests and scope

Several possible over-readings are false and are excluded from the finding.

- The lower bound (27) does **not** imply that high-conductor modes carry large `L^2` energy. WI-059 proves the opposite once the exponent grows at the scale (24). Wiener mass and squared Fourier mass answer different questions.
- The result does **not** show that individual additive twists at conductors `d<=D_w=X^{o(1)}` are inaccessible. It shows that even excellent bounds with any fixed log-power saving cannot simply be summed absolutely against all retained coefficients.
- The result does **not** rule out a conductor-dependent saving strong enough to beat `A_w(D_w)`, nor a direct theorem whose constants improve with `X`. It closes the standard fixed-parameter/fixed-log-power black-box route.
- The estimate uses only odd primes; the exceptional local behavior at `2` therefore cannot invalidate the lower bound.
- No assumption is made that the complementary Fourier modes are statistically independent. Tensorization in (17) concerns the exact Fourier transform of the deterministic CRT product, not the prime-pair error.

The most robust next target is thus not “prove the same twisted estimate for more conductors.” It is to obtain a **collective** estimate over the retained spectrum that sees the small `l^2` mass in (36).

## 8. Prior-art audit and novelty discipline

The ingredients separated above have classical antecedents: finite Fourier tensorization over the CRT, Wiener norms, Parseval, and square-function/large-sieve principles are standard harmonic-analytic tools. The arithmetic side of the live route remains anchored in the Matomäki--Radziwiłł--Tao long-shift correlation theorem and the Shao--Teräväinen/Bienvenu small-prime-conditioning interfaces already recorded in `research/weil_inertia/SOURCES.md` and audited in WI-034, WI-037, WI-041--WI-043, WI-054, and WI-057--WI-059.

The audit did **not** find a source asserting the specific quantitative combination (21)--(31) for the retained `W`-local spectrum at the WI-059 cutoff, or the resulting no-go (34). That absence is not evidence of priority. The durable Mathia contribution claimed here is only the exact deduction from the already-audited local factors and its consequence for the current research decision tree.

## 9. Research disposition

This closes one concrete repair path after WI-059:

\[
\text{retain }d\le D_w
\to
\text{bound every additive mode separately by }(\log X)^{-A}
\to
\text{sum absolute values}.
\tag{39}
\]

The first arrow remains valid; the second may or may not be analytically obtainable; the **third arrow is the obstruction**. At the necessary retained scale, it loses a factor larger than every fixed power of `log X`.

Accordingly, the live Yang covariance clue should be attacked through one of the following mathematically distinct interfaces: a weighted `l^2` twisted estimate, a large-sieve inequality across the additive modes, exact cross-mode cancellation from the local factors, or a direct conditioned pair theorem. This finding does not by itself resolve that clue and therefore creates no clue-state churn.

**Dependencies:** WI-057 (ordinary pair discrepancy does not control `W`-local conditioned covariance); WI-058 (exact local Fourier/product law and `L^2` scale); WI-059 (necessary growing exponent and sufficient cutoff `D_w`).

**Finding gate:** passes as a decisive negative result and prior-art redirection. It rules out an otherwise natural fixed-log, per-mode assembly strategy at the quantitatively necessary conductor scale while identifying the norm structure a successful replacement must preserve.
