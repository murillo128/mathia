# MC-186 — Alamoudi's rough Möbius expansion stops at the subpower zero-mode barrier

**Status:** `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The rough Möbius zero mode isolated in `MC-180` and `MC-185` is already controlled much more strongly in current literature than the generic unconditional Mertens bound suggests, but the available estimate still stops on the wrong side of the exact fixed-power boundary required by the live short-interval variance program.

Let

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y},
\qquad
G_y(x)=\sum_{n\le x}g_y(n),
\tag{1}
\]

with the convention `P^-(1)=infinity`. In the current version of Yazan Alamoudi's 2026 preprint *On subradically sifted sums related to Alladi's higher order duality between prime factors* (arXiv:2601.10636v2, revised 3 September 2026), the displayed `k=1` base-case specialization of Theorem 1.1 gives, for every fixed positive integer `N`,

\[
\boxed{
G_y(x)
\ll_N
\frac{x}{\log x}
\left(\frac{\log y}{\log x}\right)^{N+1}
}
\tag{2}
\]

through the theorem's subradical sifting range. The paper explicitly treats `k-1=0` as the base case in Section 3, and for `k=1` the finite main sum in the second formula of Theorem 1.1 is empty, leaving precisely its stated remainder estimate.

At the logarithmic cutoff used by `MC-180`,

\[
y=c\log X,
\qquad c>0\text{ fixed},
\tag{3}
\]

and uniformly for `x\asymp X`, `(2)` becomes

\[
\boxed{
G_{c\log X}(x)
\ll_{N,c}
X\frac{(\log\log X)^{N+1}}{(\log X)^{N+2}}.
}
\tag{4}
\]

Therefore, for every fixed `A>0`, after choosing `N=N(A)` sufficiently large,

\[
\boxed{
G_{c\log X}(X),\ G_{c\log X}(2X),\
G_{c\log X}(2X)-G_{c\log X}(X)
\ll_{A,c}
\frac{X}{(\log X)^A}.
}
\tag{5}
\]

Thus the signed rough zero mode is **not merely qualitatively small**: current Selberg--Delange/rough-sum technology makes it smaller than `X` by every fixed logarithmic power at the exact logarithmic cutoff used by the Mathia rough decomposition.

However, `MC-185` proves that an uncentered rough short-interval variance estimate

\[
V_y(X,H)
\le X^{1+o(1)}H^{2-\eta},
\qquad H=X^\theta,
\qquad \eta>0,
\tag{6}
\]

requires the zero mode to satisfy

\[
G_y(2X)-G_y(X)
\ll
X^{1+o(1)}H^{-\eta/2}+H.
\tag{7}
\]

In the active range `theta<6/11` and `0<eta<=1`, the first term dominates, so `(7)` asks for

\[
\boxed{
G_y(2X)-G_y(X)
\ll
X^{1-\theta\eta/2+o(1)}.
}
\tag{8}
\]

For every fixed `A` and every fixed `delta>0`,

\[
\frac{X/(\log X)^A}{X^{1-\delta}}
=
\frac{X^\delta}{(\log X)^A}
\longrightarrow\infty.
\tag{9}
\]

Hence `(5)` does **not** imply `(8)` for any fixed positive `theta eta/2`. The live obstacle can now be stated more sharply: the missing source theorem must cross from **arbitrarily strong fixed-logarithmic cancellation** for the logarithmically rough Möbius sum to **one genuine fixed power of cancellation**.

The expansion order in Alamoudi's theorem also quantifies exactly where that jump would have to enter. Since

\[
\frac{\log y}{\log X}
=
\frac{\log\log X+O_c(1)}{\log X},
\tag{10}
\]

a remainder of the shape `(2)` could reach `X^{1-\delta}` by this mechanism only if the expansion order were allowed to grow roughly as

\[
\boxed{
N
\gtrsim
(\delta+o(1))\frac{\log X}{\log\log X}.
}
\tag{11}
\]

The theorem is instead a fixed-`N` asymptotic: its constant is explicitly allowed to depend on `N`, and the proof also makes `N` part of the contour/error construction. No uniform control remotely of the scale `(11)` is supplied. Taking `N=N(X)` in `(2)` is therefore not justified.

This gives a source-level boundary rather than a generic slogan. The rough decomposition has already bought all fixed logarithmic powers for its coarse signed mode, but the fixed-power variance currency of `MC-177`/`MC-180`/`MC-185` still requires a qualitatively stronger uniformity principle.

## 1. Exact specialization of the current rough-sum theorem

Alamoudi studies

\[
M_{k,\omega}(x,y)
=
\sum_{\substack{n\le x\\P^-(n)>y}}
\mu(n){\omega(n)-1\choose k-1}.
\tag{12}
\]

Theorem 1.1 gives a second representation

\[
M_{k,\omega}(x,y)
=
\frac{x}{\log x}
\sum_{\substack{1\le i\le N\\1\le J\le k-1\\1\le j\le J}}
\phi_{i,J}(y)
\frac{\Gamma_{i,j}}{(\log x)^i}
(\log\log x)^{J-j}{J\choose j}
+
\varepsilon'''_{N,k-1}(x,y),
\tag{13}
\]

with

\[
|\varepsilon'''_{N,k-1}(x,y)|
\le
C_{N,k-1}
\frac{x(\log\log(x+1))^{k-1}}{\log x}
\left(\frac{\log y}{\log x}\right)^{N+1}.
\tag{14}
\]

For `k=1`, `(12)` is exactly `G_y(x)`. The main sum in `(13)` is empty because it requires `1<=J<=0`, while the factor `(log log(x+1))^(k-1)` in `(14)` is `1`. This gives `(2)` directly.

There is no range conflict at `(3)`. For fixed `c`, `c log X` is eventually far below the theorem's permitted upper sifting scale

\[
Y_0\exp\!\left(p\frac{\log x}{(\log\log(x+1))^{1+\epsilon}}\right)
\tag{15}
\]

for any fixed admissible positive parameters, and `x\asymp X`. Thus the specialization genuinely covers the moving logarithmic cutoff used by `MC-180`.

To obtain `(5)`, fix `A`. Choose a fixed `N` large enough that

\[
\frac{(\log\log X)^{N+1}}{(\log X)^{N+2}}
\ll_A
(\log X)^{-A}.
\tag{16}
\]

Applying `(4)` at `X` and `2X` and using the triangle inequality proves the increment bound in `(5)`. No zero-free half-plane of fixed width and no RH-scale estimate is imported in this deduction.

## 2. Why all fixed logarithmic powers are still insufficient

`MC-185` did not merely observe that a centered parity deformation has an inconvenient mean. It derived the exact identity

\[
X\overline P_X(-1)
=
H\bigl(G_y(2X)-G_y(X)\bigr)+O(H^2+H),
\tag{17}
\]

so the rough increment is the literal zero-frequency component omitted by centered variance. To make that component fit `(6)`, `(7)` is necessary at the target scale.

For `H=X^theta`, write

\[
\delta=\frac{\theta\eta}{2}>0.
\tag{18}
\]

Because the active support-variance range has `theta<6/11<2/3` and `eta<=1`, one has `1-delta>theta`; hence the `H` term in `(7)` is lower order at the fixed-power level. The target is therefore `(8)`.

Equation `(9)` is the decisive rate comparison. The family of estimates `(5)` is often informally described as "better than any logarithmic power", but it remains of size `X^{1-o(1)}`. The target `(8)` is `X^{1-delta+o(1)}` with `delta` fixed. Those are different asymptotic currencies, and no choice of **fixed** `A` crosses the gap.

This also explains why merely asking for more terms of the fixed-order Selberg--Delange expansion is not enough. If `N` remains fixed while `X` grows, every extra term only improves a logarithmic power. To make

\[
\left(\frac{\log\log X}{\log X}\right)^N
\lesssim X^{-\delta},
\tag{19}
\]

taking logarithms forces `(11)` up to lower-order `log log log X` terms. The missing theorem would therefore need growing-order control of the entire expansion, including its `N`-dependent constants and contour errors, or a different source mechanism that creates a fixed power directly.

## 3. The source itself exposes the analytic method boundary

The same preprint makes clear that the obstruction is not an accidental loss in the preceding algebra. Its Selberg--Delange setup factors the rough square-free generating function as

\[
f(s,y,z)
=
z^{-1}\prod_{p>y}(1+zp^{-s})
=
g(s,y,z)\zeta(s)^z,
\tag{20}
\]

and differentiation at `z=-1` recovers the signed rough Möbius coefficients. In the proof, the resulting integrand contains `1/\zeta(s)` and is handled on a contour whose leftward displacement is of zero-free-region type rather than a fixed-width excursion into the critical strip.

Section 5 is especially diagnostic. When discussing faster sifting, the paper notes that Buchstab iteration gives insight in the `k=1` Alladi case, but also states that classical bounds for the relevant `g(s,y,-1)` produce a "stubborn error term" and that the author therefore avoids an incursion into the interior of the critical strip for the general sifting region.

This does not prove an impossibility theorem for Selberg--Delange or Buchstab methods. It does identify the current theorem's source of asymptotic currency: a narrowing neighborhood of `Re(s)=1` naturally supports logarithmic/subpower savings, while the Mathia target demands a fixed exponent. Any claimed upgrade of `(2)` to `(8)` must therefore exhibit the new uniform ingredient rather than treating higher fixed expansion order as sufficient.

## 4. Prior art and novelty boundary

The rough Möbius function is classical. Alladi's 1982 paper *Asymptotic estimates of sums involving the Moebius function* studies

\[
M(x,y)=\sum_{\substack{n\le x\\P^-(n)>y}}\mu(n),
\]

and `MC-180` already records Alladi, Hazlewood, and related restricted-prime-factor work as prior art. No novelty is claimed for the object, for Buchstab iteration, for Selberg--Delange analysis, or for Alamoudi's theorem.

The current source used here is:

- Yazan Alamoudi, *On subradically sifted sums related to Alladi's higher order duality between prime factors*, arXiv:2601.10636v2, revised 3 September 2026, https://arxiv.org/abs/2601.10636.

The Mathia contribution is only the **rate audit against the already-derived zero-mode obligation of `MC-185`**: `(2)` specializes the newest rough-sum expansion to the exact logarithmic cutoff, `(5)` records the strongest immediate asymptotic class it supplies, and `(9)`--`(11)` identify the quantitative uniformity jump still missing before it can feed the fixed-power variance mechanism.

## 5. Boundaries and falsification tests

- The finding does not claim a new estimate for rough Möbius sums. Equations `(2)`--`(5)` are direct specializations/consequences of Alamoudi's current theorem.
- The theorem is used only inside its stated subradical sifting range; `y=c log X` lies safely inside that range for fixed `c` and large `X`.
- The argument does not set `N` as a function of `X`. The source constant depends on `N`; doing so without new uniform estimates would invalidate the deduction.
- "Smaller than every fixed logarithmic power" must not be restated as `X^{1-delta}` for any fixed `delta>0`. Equation `(9)` is the explicit falsification check against that upgrade.
- The source-level contour discussion is a method boundary, not a no-go theorem. A strengthened Selberg--Delange/Buchstab argument with new uniform estimates, or an unrelated parity-sensitive bilinear mechanism, remains open.
- No estimate for the full rough short-interval second moment `(6)` follows from `(5)`. The zero mode is only one necessary component of that variance target.
- No new bound for the ordinary Mertens function or the zeta zero set is claimed.

The finding is falsified if the `k=1` base-case specialization of the current Theorem 1.1 does not reduce to `(2)`, if `y=c log X` falls outside its stated range, if `(4)` fails to imply `(5)` for every fixed `A`, or if some fixed logarithmic saving can imply the fixed-power target `(8)` without additional information.

## Consequence for the active frontier

`MC-185` left three plausible ways to repair the parity-deformation route: control the signed zero mode independently, couple it to the fluctuating statistic before centering, or abandon that representation for a parity-sensitive Type-II/bilinear mechanism. The present source audit materially narrows the first option.

The zero mode already enjoys **arbitrarily strong fixed-logarithmic cancellation** at `y=c log X`. Reproving another `X/log^A X` estimate, even for very large fixed `A`, does not buy the fixed-power currency needed by `MC-177`. A useful next theorem must instead explain one of two genuinely stronger transitions: either a growing-order uniformity mechanism on the scale `N \asymp log X/log log X`, with all constants and contour errors controlled, or a source-side cancellation principle that produces a fixed power without passing through fixed-order asymptotic expansion.

That is now the precise source-side frontier for the coarse rough mode. The remaining local-variance problem is harder still: even after the zero mode is upgraded, the off-diagonal rough parity field must retain enough signed coupling to satisfy the full variance target of `MC-180`.