# NB-009 — one parity normal equation forces polylogarithmic residual witness localization

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + RESIDUAL-SPECIFIC-LOCALIZATION + PARITY-NORMAL-EQUATION + SUB-LCM-CERTIFICATE + POLYLOGARITHMIC-SCALE-CONSEQUENCE`. `NB-008` proves that every finite best residual has a tail-average witness by using the common period `lcm(2,...,N)`, but that mechanism places the witness at exponential index. The actual projection residual satisfies much stronger source equations than an arbitrary vector in the target-augmented finite space. Already the single normal equation against the generator `g_2` removes the lcm cost.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
r_N=e-P_{V_N}e,
\qquad
d_N=\|r_N\|,
\qquad a_N=d_N^2,
\]

and retain

\[
c_n(h)=n\int_0^{1/n}h(x)\,dx,
\qquad
\Gamma_B(r_N)=
\max_{1\le n\le B}\frac{|c_n(r_N)-a_N|^2}{n}.
\tag{1}
\]

Put

\[
s_*:=\log2-\frac14>0.
\tag{2}
\]

For every `N>=2`, let `K_N` be the least even integer satisfying

\[
K_N\ge \frac{4}{a_Ns_*^2}.
\tag{3}
\]

Then

\[
\boxed{
K_N\le \frac{6}{s_*^2d_N^2},
\qquad
\Gamma_{K_N}(r_N)
\ge \frac{s_*^4}{96}\,d_N^6.
}
\tag{4}
\]

Thus the actual best residual has a quantitatively nonconstant normalized tail average by index `O(d_N^{-2})`, with amplitude polynomial in its distance. No common period, Gram condition number, finite observation-matrix inversion, or Mellin-bandwidth hypothesis enters this localization.

Burnol's zero-sensitive Nyman lower bound then turns (4) into a genuine scale statement in the section size. The discrete space is contained in the corresponding continuous Nyman space at cutoff `lambda=1/N`, so `d_N` is no smaller than the continuous distance. Consequently there are constants `C_1,C_2>0` such that, for all sufficiently large `N`,

\[
\boxed{
K_N\le C_1\log N,
\qquad
\Gamma_{K_N}(r_N)\ge\frac{C_2}{(\log N)^3}.
}
\tag{5}
\]

The exponential lcm scale in `NB-008` is therefore not intrinsic to the best residual. A **single low-order source normal equation** forces a witness at polylogarithmic index. This does not improve the known Nyman approximation distance: the `1/log N` input in (5) is precisely a known zero-sensitive lower bound. The new content is that the canonical residual must expose that non-target mass to the tail-average/semigroup observable much earlier than periodicity alone can see it.

## 1. The `g_2` normal equation is an exact odd-shell cancellation law

Use Bagchi's harmonic intervals

\[
I_n=\left(\frac1{n+1},\frac1n\right]
\]

and the exact generator values

\[
g_l|_{I_n}=\left\{\frac nl\right\}.
\tag{6}
\]

For `l=2`,

\[
g_2|_{I_n}=
\begin{cases}
\frac12,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}
\tag{7}
\]

Because `N>=2`, best approximation gives the exact normal equation

\[
\langle r_N,g_2\rangle=0.
\]

Writing `r_{N,n}` for the value of `r_N` on `I_n` and using
`|I_n|=1/[n(n+1)]`, this becomes

\[
\boxed{
\sum_{n\ \mathrm{odd}}
\frac{r_{N,n}}{n(n+1)}=0.
}
\tag{8}
\]

The corresponding total odd-shell measure is the alternating harmonic series:

\[
\boxed{
\sum_{n\ \mathrm{odd}}\frac1{n(n+1)}=\log2.
}
\tag{9}
\]

Thus a residual whose early harmonic shells looked approximately like the positive constant `a_N` would have to cancel a fixed mass `a_N log 2` using either early tail-average variation or its remote Hilbert tail. The norm `d_N` makes the second option quantitatively expensive.

## 2. Tail averages reconstruct the shell values with no conditioning loss

Orthogonal projection also gives

\[
c_1(r_N)=\langle r_N,e\rangle=\|r_N\|^2=a_N.
\tag{10}
\]

Set

\[
\delta_n=c_n(r_N)-a_N.
\tag{11}
\]

The reconstruction identity already used in `NB-004` and `NB-008` is

\[
r_{N,n}=(n+1)c_n(r_N)-nc_{n+1}(r_N),
\]

hence

\[
\boxed{
r_{N,n}-a_N=(n+1)\delta_n-n\delta_{n+1}.}
\tag{12}
\]

Let `M>=3` be odd and put `K=M+1`. Split (8) at `M`. The odd weight captured before the split satisfies

\[
S_M:=\sum_{\substack{n\le M\\n\ \mathrm{odd}}}
\frac1{n(n+1)}
\ge \log2-\frac1K,
\tag{13}
\]

because the total weight after `M` is at most `sum_(n>M)1/[n(n+1)]=1/K`.

For the remote residual itself, Cauchy--Schwarz and `||r_N||=d_N` give

\[
\left|
\sum_{\substack{n>M\\n\ \mathrm{odd}}}
\frac{r_{N,n}}{n(n+1)}
\right|
\le
\frac{d_N}{\sqrt K}.
\tag{14}
\]

The early deviation has a particularly clean form. Multiplying (12) by the shell weight gives

\[
\frac{r_{N,n}-a_N}{n(n+1)}
=\frac{\delta_n}{n}-\frac{\delta_{n+1}}{n+1}.
\tag{15}
\]

As `n` runs through the odd integers `1,3,...,M`, the two indices in (15) cover every integer `1,...,K` exactly once. If

\[
G_K:=\Gamma_K(r_N),
\]

then `|delta_j|<=sqrt(jG_K)` and therefore

\[
\begin{aligned}
\left|
\sum_{\substack{n\le M\\n\ \mathrm{odd}}}
\frac{r_{N,n}-a_N}{n(n+1)}
\right|
&\le
\sqrt{G_K}\sum_{j=1}^{K}\frac1{\sqrt j}\\
&\le2\sqrt{KG_K}.
\end{aligned}
\tag{16}
\]

Combining (8), (13), (14), and (16) yields the exact finite inequality

\[
\boxed{
2\sqrt{KG_K}
\ge
\left[
a_N\left(\log2-\frac1K\right)
-\frac{d_N}{\sqrt K}
\right]_+.
}
\tag{17}
\]

This estimate is valid for every even `K>=4`; the chosen scale (3) is only one convenient specialization.

## 3. Choosing `K` at the inverse-distance scale proves the polynomial modulus

For the `K_N` of (3), `K_N>=4`, so

\[
\log2-\frac1{K_N}\ge s_*.
\tag{18}
\]

Moreover

\[
\frac{d_N}{\sqrt{K_N}}
\le\frac{a_Ns_*}{2}.
\tag{19}
\]

Equation (17) therefore gives

\[
2\sqrt{K_N\Gamma_{K_N}(r_N)}
\ge\frac{a_Ns_*}{2},
\]

or

\[
\Gamma_{K_N}(r_N)
\ge\frac{a_N^2s_*^2}{16K_N}.
\tag{20}
\]

Minimality among even integers gives

\[
K_N<\frac4{a_Ns_*^2}+2
\le\frac6{a_Ns_*^2},
\tag{21}
\]

where the final inequality uses `a_Ns_*^2<1`. Substitution into (20) proves (4):

\[
\Gamma_{K_N}(r_N)
\ge\frac{s_*^4}{96}a_N^3
=\frac{s_*^4}{96}d_N^6.
\tag{22}
\]

The scaling is worth separating from the constants. The remote tail can contribute at most `d_N/sqrt(K)`, while the forced odd-shell mean is of order `d_N^2`. They become comparable at `K asymp d_N^{-2}`. At that scale, the reconstruction map converts the remaining fixed fraction of the odd-shell cancellation into `Gamma_K asymp d_N^6`. The lcm never appears because the proof uses projection orthogonality rather than simultaneous zeros of all generators.

## 4. Burnol converts inverse-distance localization into logarithmic index localization

Burnol's quantitative Nyman theorem, already anchored in `SOURCES.md`, gives a positive zero-sensitive lower-bound constant for the continuous approximation distance `D(lambda)`:

\[
\liminf_{\lambda\downarrow0}
|\log\lambda|\,D(\lambda)^2>0.
\tag{23}
\]

More precisely his theorem records the contribution of critical zeros with squared multiplicities. If RH fails, the scaled continuous distance is instead unbounded, so the positive lower-bound consequence remains valid.

Under the canonical Nyman--Bagchi equivalence, the discrete section `V_N` uses only the integer parameters `1/l`, `2<=l<=N`, and is contained in the continuous admissible space with cutoff `lambda=1/N`. Hence

\[
\boxed{d_N\ge D(1/N).}
\tag{24}
\]

It follows that there is `c_B>0` such that, for all sufficiently large `N`,

\[
d_N^2\ge\frac{c_B}{\log N}.
\tag{25}
\]

Combining (21)--(22) with (25) gives (5), for example with constants depending only on `c_B` and `s_*`.

This use of Burnol is deliberately one-way. The new parity argument does **not** reprove the zero-sensitive distance floor. Instead it says that whatever non-target mass that classical theorem forces into the best residual cannot hide from all early normalized tail averages: one witness occurs by logarithmic index and has at least cubic-logarithmic normalized amplitude.

## 5. Consequence for the harmonic semigroup observable

`NB-007` gives, for every `h`, every index `n`, and every `X>=2n`,

\[
\mathcal E_X(h)
\ge
\frac{|c_n(h)-c_1(h)|^2}{4n}
\left(H_{\lfloor X/n\rfloor}-1\right).
\tag{26}
\]

Choose an index `n<=K_N` attaining `Gamma_(K_N)(r_N)`. Since the harmonic factor decreases with `n`, for every `X>=2K_N`,

\[
\boxed{
\mathcal E_X(r_N)
\ge
\frac{s_*^4}{384}d_N^6
\left(H_{\lfloor X/K_N\rfloor}-1\right).
}
\tag{27}
\]

Using Burnol, one may take `K_N=O(log N)` and the prefactor is `Omega((log N)^-3)`. For polynomial `X=N^theta`, the harmonic factor is of order `log N`, so (27) supplies a lower bound of order `(log N)^-2` for the truncated source defect.

This is a finite-depth, source-selected statement that `NB-006`'s arbitrary Mellin aliases cannot contradict: those aliases do not satisfy the best-residual normal equation (8). It also explains exactly which extra structure defeats the recurrence obstruction. No growing family of normal equations is required for localization; the fixed generator `g_2` is enough because its support occupies a positive harmonic-shell density while the residual has controlled total norm.

Equation (27) is still only a **lower** source-defect estimate. No comparably sharp source-derived upper estimate is proved here, so it does not squeeze `d_N` to a new rate or imply RH.

## 6. Prior art, falsification controls, and research consequence

The load-bearing literature inputs are already in `research/nyman_beurling/SOURCES.md`: Bagchi supplies the exact harmonic-interval generator model, while Burnol supplies the zero-sensitive lower-bound scale. The finite cancellation argument (8)--(22) uses only the first generator normal equation, the exact reconstruction identity, the alternating harmonic series, and Cauchy--Schwarz.

A targeted prior-art search covering Burnol's quantitative bounds, Bagchi/Báez--Duarte finite sections, Ehm's 2024 Gram-matrix analysis, Nyman residuals, and parity/odd-shell formulations did not locate the specific estimate (17) or an `O(d_N^-2)` tail-average localization theorem. This search absence is not used as proof of novelty. Ehm's Gram formulas are a neighboring finite-section analysis, but the present mechanism is explicitly target/residual-aware: it disappears for arbitrary vectors sharing the generator Gram geometry.

Several boundaries are essential. First, (4) is a theorem about the **best residual** and uses `r_N perpendicular g_2`; it does not contradict the late-shell controls in `NB-007`. Second, the logarithmic-in-`N` corollary uses the known Burnol floor and therefore is not an independent improvement of the Nyman distance. Third, the exponent `d_N^6` is a sufficient consequence of one parity probe, not an optimal modulus; additional normal equations may improve it. Fourth, (27) is not useful by itself unless paired with an upper control on the same semigroup defect or another implication for `d_N`.

The durable frontier has therefore moved past the lcm localization barrier. Finite best residuals cannot postpone all target-aware tail mismatch to exponential index: one exact low-order normal equation forces a witness by `O(d_N^-2)`, hence by `O(log N)` on the classical zero-sensitive scale. The next quantitative gate is to determine whether the remaining normal equations yield a stronger modulus/location tradeoff, or whether the truncated harmonic semigroup defect admits a residual-specific upper estimate sharp enough to turn (27) into new information about `d_N`.