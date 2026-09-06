# MC-113 — Chebyshev minimax forces logarithmic range for uniform proportional-shell attenuation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the proportional Hamming-shell profile of `MC-107` and the local-filter transfer interpretation of `MC-111`--`MC-112`. For a fixed proportional shell

\[
\beta=\frac{k-2}{2\log\log N},
\]

`MC-107` gives the local ratio

\[
\frac{C_{k+1,N}}{C_{k,N}}\to \beta^{-1}.
\]

Thus the compact proportional range

\[
\frac12\le \beta\le2
\tag{1}
\]

corresponds to the ideal local-ratio band

\[
I:=\left[\frac12,2\right].
\tag{2}
\]

For a real polynomial transfer filter

\[
A(x)=\sum_{j=0}^{r}a_jx^j
\tag{3}
\]

that retains the parity endpoint, `MC-111` requires

\[
A(-1)\ne0.
\tag{4}
\]

Normalize by parity and write

\[
P(x):=\frac{A(x)}{A(-1)},
\qquad P(-1)=1.
\tag{5}
\]

Then the exact minimax problem on the entire proportional-shell ratio band is

\[
\boxed{
\inf_{\substack{\deg P\le r\\P(-1)=1}}
\ \sup_{x\in[1/2,2]}|P(x)|
=\frac1{T_r(3)},
}
\tag{6}
\]

where `T_r` is the Chebyshev polynomial of the first kind. Equality is attained by

\[
\boxed{
P_r^*(x)=
\frac{T_r\!\left((4x-5)/3\right)}{T_r(-3)}.
}
\tag{7}
\]

Since

\[
T_r(3)
=\cosh\!\bigl(r\,\operatorname{arcosh}3\bigr)
=\frac{(3+\sqrt8)^r+(3-\sqrt8)^r}{2},
\tag{8}
\]

we obtain

\[
\frac1{T_r(3)}
=\exp\!\left(-r\log(3+\sqrt8)+O(1)\right).
\tag{9}
\]

Consequently, if an `N`-dependent polynomial filter of degree `r_N` is required to suppress **every** ideal proportional-shell ratio in `(2)` by a fixed power while retaining parity,

\[
\sup_{x\in[1/2,2]}
\frac{|A_N(x)|}{|A_N(-1)|}
\le N^{-\delta}
\qquad(\delta>0\text{ fixed}),
\tag{10}
\]

then necessarily

\[
\boxed{
r_N\ge
\frac{\delta}{\log(3+\sqrt8)}\log N+O(1).
}
\tag{11}
\]

Conversely, the Chebyshev optimizer `(7)` achieves attenuation of order

\[
2(3+\sqrt8)^{-r},
\tag{12}
\]

so the logarithmic degree scale is sharp for this **transfer-polynomial minimax problem**.

Therefore the `N`-dependent-filter escape left open by `MC-112` cannot obtain a fixed polynomial gain by uniformly flattening the proportional-shell ratio band with a sublogarithmic-degree transfer polynomial. If

\[
r_N=o(\log N),
\tag{13}
\]

then for every such parity-normalized filter there exists some

\[
x_N\in[1/2,2]
\]

with

\[
\boxed{
\frac{|A_N(x_N)|}{|A_N(-1)|}
\ge N^{-o(1)}.
}
\tag{14}
\]

This is an exact filter-design obstruction. It does **not** yet assert that the actual growing-range source convolution

\[
T_{k,N}^{A_N}=\sum_{j=0}^{r_N}a_{j,N}C_{k+j,N}
\]

is asymptotic to `A_N(\beta^{-1})C_{k,N}` when `r_N\to\infty`; `MC-107`--`MC-112` establish the required source transfer only for fixed shifts/filters. Uniform growing-shift Sathe--Selberg control, coefficient conditioning, and signed reconstruction remain separate proof obligations. No estimate for `M(x)` is improved here.

## 1. Affine rescaling turns the shell band into the Chebyshev interval

Map `(2)` to `[-1,1]` by

\[
u=\frac{4x-5}{3},
\qquad
x=\frac{3u+5}{4}.
\tag{15}
\]

The parity point `x=-1` maps to

\[
u_0=-3.
\tag{16}
\]

For any admissible `P`, define

\[
Q(u)=P\!\left(\frac{3u+5}{4}\right).
\tag{17}
\]

Then `deg Q<=r`, `Q(-3)=1`, and

\[
\|Q\|_{L^\infty[-1,1]}
=
\|P\|_{L^\infty[1/2,2]}.
\tag{18}
\]

The problem is therefore exactly: among real polynomials of degree at most `r` with prescribed value `1` at the exterior point `-3`, minimize the uniform norm on `[-1,1]`.

## 2. Chebyshev alternation gives the exact exterior-point minimax

The classical Chebyshev polynomial satisfies

\[
T_r(\cos\theta)=\cos(r\theta)
\tag{19}
\]

and therefore takes alternating values `(-1)^j` at the `r+1` extrema

\[
u_j=\cos(j\pi/r),
\qquad j=0,\dots,r.
\tag{20}
\]

Set

\[
Q_r^*(u)=\frac{T_r(u)}{T_r(-3)}.
\tag{21}
\]

Then `Q_r^*(-3)=1` and

\[
\|Q_r^*\|_{L^\infty[-1,1]}
=\frac1{|T_r(-3)|}
=\frac1{T_r(3)}.
\tag{22}
\]

To prove optimality directly, suppose another admissible `Q` had strictly smaller norm. At each `u_j`, the difference

\[
R(u)=Q(u)-Q_r^*(u)
\]

has the opposite sign from `Q_r^*(u_j)`, because `|Q(u_j)|<|Q_r^*(u_j)|`. Hence `R` changes sign in every interval between consecutive extrema and has at least `r` distinct zeros in `(-1,1)`. It also has the exterior zero

\[
R(-3)=Q(-3)-Q_r^*(-3)=0.
\]

That gives at least `r+1` distinct zeros for a polynomial of degree at most `r`, a contradiction. The usual non-strict alternation argument gives the extremal value `(22)` and the Chebyshev optimizer. Rescaling back by `(15)` proves `(6)`--`(7)`.

This is the standard Chebyshev exterior-growth/minimax mechanism, not a new approximation-theory theorem.

## 3. A fixed power of attenuation costs order `log N` shell range

Let

\[
\lambda:=3+\sqrt8>1.
\tag{23}
\]

Equation `(8)` gives

\[
T_r(3)=\frac{\lambda^r+\lambda^{-r}}2.
\tag{24}
\]

If `(10)` holds, the exact minimax lower bound `(6)` forces

\[
T_{r_N}(3)\ge N^\delta.
\tag{25}
\]

Since `T_r(3)<\lambda^r` for `r>=1`,

\[
r_N\log\lambda>\delta\log N,
\tag{26}
\]

which is `(11)` up to an immaterial endpoint constant. Conversely `(24)` and the optimizer `(7)` give `(12)`, so the `Theta(log N)` threshold is not an artifact of a loose inequality.

This sharply separates two scales in the current Hamming branch. The shell mass itself is organized at degree `Theta(log log N)` by `MC-107`--`MC-109`, but a transfer polynomial that tries to suppress a whole fixed proportional band by `N^{-delta}` while preserving the parity value at `-1` needs degree `Theta(log N)`. In degree space this is parametrically larger than both the turning location `2 log log N` and its `sqrt(log log N)` central width.

The conclusion is only about uniform transfer-function suppression. A source-specific signed recurrence could evade the minimax setup by exploiting relations among the actual `C_{k,N}` rather than demanding small polynomial response at every local-ratio frequency.

## 4. Prior art and novelty boundary

The approximation-theory input is classical. NIST DLMF §18.38(i), *Approximation Theory*, records the minimax property of Chebyshev polynomials on `[-1,1]` and points to Mason--Handscomb, Cheney, and Rivlin for the classical theory. DLMF §3.11(ii) records

\[
T_r(x)=\cos(r\arccos x)
\]

on `[-1,1]`, the affine rescaling to a general interval, and the equioscillation structure underlying minimax approximation. The exterior-point form used above follows by the standard alternation argument written explicitly in Section 2. Generic FIR/equiripple filter design also uses the same Chebyshev minimax mechanism.

Targeted searches for the combination of Chebyshev/equiripple filter bounds with the specific Möbius Hamming-shell deformation and the proportional Sathe--Selberg ratio band found only the generic approximation/filtering mechanism, not a source-specific theorem. **No novelty claim is made.** The durable delta is the application of the exact classical minimax constant to the previously open growing-filter branch of the persisted Mathia shell model.

Authoritative references:

- NIST Digital Library of Mathematical Functions, §18.38(i), *Classical OP's: Numerical Analysis — Approximation Theory*, https://dlmf.nist.gov/18.38.i.
- NIST Digital Library of Mathematical Functions, §3.11(ii), *Chebyshev-Series Expansions*, https://dlmf.nist.gov/3.11.ii.

## 5. Boundaries and falsification tests

- The theorem is stated for **real polynomial filters**, matching `MC-111`--`MC-112`. Complex-valued filters are not classified here.
- The compact band `[1/2,2]` is a convenient fixed proportional-shell range, not a claimed optimal choice. Any fixed positive ratio interval separated from the parity point has an analogous Chebyshev/conformal extremal constant after affine rescaling.
- The degree lower bound concerns a filter that seeks **uniform** fixed-power attenuation of the ideal local-ratio transfer function across the whole band. It does not rule out a filter tuned to a smaller moving set of ratios, a source-specific recurrence, or a signed transform that never takes uniform absolute values.
- Most importantly, no uniform growing-shift source asymptotic is assumed. For `r_N\to\infty`, replacing the actual response `T^{A_N}_{k,N}/C_{k,N}` by `A_N(\beta^{-1})` requires new control of shifted shell ratios together with the coefficient norm/conditioning of `A_N`. The present result is a necessary design-budget obstruction before that harder arithmetic step, not a surrogate for it.
- A degree `Theta(log N)` Chebyshev filter is extremal only at the transfer-polynomial level. Its coefficients can be large, its range extends far beyond the natural `Theta(log log N)` shell turning scale, and nothing here shows that it produces a useful Möbius endpoint certificate after exact source convolution and reconstruction.
- The finding does not improve the unconditional Mertens bound, prove RH, or identify the signed source relation that creates the actual endpoint cancellation.

A decisive falsifier of `(6)` would be a real polynomial of degree at most `r`, equal to `1` at `-1`, whose sup norm on `[1/2,2]` is strictly below `1/T_r(3)`. The alternation proof in Section 2 rules this out exactly.

## Consequence for the research line

`MC-112` left `N`-dependent/growing-range local filters as a formal radial escape. The first quantitative question for that escape is now classified: **sublogarithmic degree cannot buy a fixed polynomial uniform attenuation across even one fixed proportional-shell band while retaining parity**. The optimal transfer design is already Chebyshev and pays `Theta(log N)` degree for `N^{-delta}` attenuation.

A surviving growing-filter route must therefore either accept at least logarithmic range and then solve the still-open source-uniformity/conditioning/reconstruction problem, or avoid uniform local-frequency suppression altogether by preserving a genuinely signed nonlocal or source-coupled relation.