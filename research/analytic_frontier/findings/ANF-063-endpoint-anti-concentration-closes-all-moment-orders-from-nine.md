# ANF-063 — endpoint anti-concentration closes every Montgomery--Taylor moment order from nine onward

**Status:** `EXACT-DERIVED + GLOBAL-FOURIER-ANTI-CONCENTRATION + ALL-FREQUENCY-MOMENT-BOUND + FINITE-ORDER-REDUCTION + STRUCTURAL-STRENGTHENING`. `ANF-062` proves the fixed Montgomery--Taylor five-point defect is positive but leaves open the stronger all-height coercivity mechanism proposed in `CLUE-even-moment-radial-coercivity`. For

\[
M_n(t):=\int_{-1}^{1}\alpha^{2n}J_{\rm MT}(\alpha)
\cos(2\pi\alpha t)\,d\alpha,
\qquad n\ge2,
\tag{1}
\]

the clue asks whether

\[
\frac{M_n(t)}{M_n(0)}
\ge
-\frac{2^{2n-1}}{1+2^{2n-1}}
\qquad(t\in\mathbb R)
\tag{2}
\]

holds for every order. The large-order part can be closed analytically **without any horizontal-frequency cutoff**:

\[
\boxed{
\frac{M_n(t)}{M_n(0)}
>
-\frac{2^{2n-1}}{1+2^{2n-1}}
\quad
\text{for every }n\ge9\text{ and every }t\in\mathbb R.
}
\tag{3}
\]

Hence the accepted all-moment route is reduced to exactly the seven orders

\[
\boxed{n=2,3,4,5,6,7,8.}
\tag{4}
\]

The mechanism is elementary: the exact Montgomery--Taylor density is comparable to `1-x` up to the support endpoint. After normalizing `x^(2n)J_MT(x)` to a probability density, a fixed shell of width `asymp 1/n` near `x=1` has density `asymp n`. A cosine that is nearly `-1` at one point cannot remain so across that shell, yielding an `Omega(n^-2)` gap from `-1`. The target gap in (2) is exponentially smaller, of order `4^-n`.

## 1. Global endpoint comparison

On `0<=x<=1`, `ANF-062` gives

\[
J_{\rm MT}(x)
=
\frac{(1-x)\cos(\sqrt2 x)
      +\sin(\sqrt2(1-x))/\sqrt2}
     {4\sin^2(1/\sqrt2)}.
\tag{5}
\]

Because `0<=sqrt(2)x<=sqrt(2)<pi/2`, cosine is positive and decreasing there; also `0<=sin u<=u` for the second term. Thus, with

\[
c_0:=\frac{\cos\sqrt2}{4\sin^2(1/\sqrt2)},
\qquad
C_0:=\frac1{2\sin^2(1/\sqrt2)},
\tag{6}
\]

one has the exact whole-support comparison

\[
\boxed{
c_0(1-x)\le J_{\rm MT}(x)\le C_0(1-x),}
\qquad
\frac{c_0}{C_0}=\frac{\cos\sqrt2}{2}.
\tag{7}
\]

Put

\[
D_n:=\int_0^1x^{2n}J_{\rm MT}(x)\,dx,
\qquad
p_n(x):=\frac{x^{2n}J_{\rm MT}(x)}{D_n}.
\tag{8}
\]

The beta integral and (7) give

\[
D_n\le\frac{C_0}{(2n+1)(2n+2)}.
\tag{9}
\]

Evenness of `J_MT` turns the normalized moment into

\[
R_n(t):=\frac{M_n(t)}{M_n(0)}
=\int_0^1p_n(x)\cos(2\pi tx)\,dx.
\tag{10}
\]

## 2. A phase-independent endpoint-shell bound

Take

\[
I_n=
\left[1-\frac{8}{5n},\;1-\frac{2}{5n}\right],
\qquad
L:=|I_n|=\frac{6}{5n}.
\tag{11}
\]

For every `x in I_n`, (7)--(9) imply

\[
\boxed{
p_n(x)\ge
\frac{\cos\sqrt2}{5n}(2n+1)(2n+2)
\left(1-\frac{8}{5n}\right)^{2n}.}
\tag{12}
\]

For an arbitrary interval `I` of length `L`, direct integration gives

\[
\int_I\cos^2(\pi tx)\,dx
\ge
\frac L2\left(1-\frac{|\sin z|}{z}\right),
\qquad z:=\pi|t|L.
\tag{13}
\]

We use the elementary global inequality

\[
\boxed{1-\frac{|\sin z|}{z}\ge\frac{19}{120}\min(z^2,1),\qquad z>0.}
\tag{14}
\]

For `0<z<=1`, the alternating Taylor estimate

\[
\frac{\sin z}{z}
\le1-\frac{z^2}{6}+\frac{z^4}{120}
\le1-\frac{19}{120}z^2
\tag{15}
\]

proves (14). For `1<=z<=6/5`, `sin z/z` is positive and decreasing because

\[
\sin z-z\cos z=\int_0^z u\sin u\,du>0
\qquad(0<z<\pi),
\tag{16}
\]

so

\[
\frac{\sin z}{z}\le\sin1
<1-\frac16+\frac1{120}
=\frac{101}{120}.
\tag{17}
\]

For `z>=6/5`, simply

\[
\frac{|\sin z|}{z}\le\frac1z\le\frac56<\frac{101}{120}.
\tag{18}
\]

This completes the proof of (14).

If `|t|<=1/4`, then `cos(2 pi t x)>=0` on `[0,1]`, hence `R_n(t)>=0` and (2) is automatic. If `|t|>=1/4`, then with the `L` in (11),

\[
\min(z^2,1)\ge\frac{9\pi^2}{100n^2},
\tag{19}
\]

because `3pi/(10n)<1`. Equations (13)--(14) therefore yield

\[
\boxed{
\int_{I_n}\cos^2(\pi tx)\,dx
\ge\frac{171\pi^2}{20000n^3}.}
\tag{20}
\]

Using `1+cos(2u)=2cos^2u`, (10), (12), and (20) now give the all-frequency lower bound

\[
\boxed{
1+R_n(t)\ge L_n:=
\frac{171\pi^2\cos\sqrt2}{50000}
\frac{(2n+1)(2n+2)}{n^4}
\left(1-\frac{8}{5n}\right)^{2n}
}
\tag{21}
\]

for every `|t|>=1/4`.

## 3. Polynomial anti-concentration beats the exponential target from `n=9`

Write the target as

\[
-\frac{2^{2n-1}}{1+2^{2n-1}}
=-1+\delta_n,
\qquad
\delta_n:=\frac1{1+2^{2n-1}}<\frac2{4^n}.
\tag{22}
\]

The rational estimates

\[
\pi^2>9,
\qquad
\cos\sqrt2>
1-1+\frac4{24}-\frac8{720}
=\frac7{45}>\frac3{20}
\tag{23}
\]

turn (21) into

\[
L_n>
\frac{4617}{10^6}
\frac{(2n+1)(2n+2)}{n^4}
\left(1-\frac{8}{5n}\right)^{2n}.
\tag{24}
\]

At `n=9`, direct integer comparison after clearing denominators gives

\[
\frac{4617}{10^6}
\frac{380}{6561}
\left(\frac{37}{45}\right)^{18}
>
\frac1{131072}
=
\frac2{4^9}.
\tag{25}
\]

The factor

\[
a_n:=\left(1-\frac{8}{5n}\right)^{2n}
\tag{26}
\]

is increasing for `n>8/5`: differentiating `2x log(1-8/(5x))` reduces the sign to

\[
\log(1-z)+\frac{z}{1-z}>0,
\tag{27}
\]

whose derivative is `z/(1-z)^2>0` and whose limit at zero is zero. Also

\[
4^n\frac{(2n+1)(2n+2)}{n^4}
\tag{28}
\]

is increasing for `n>=4`, because the consecutive ratio is strictly larger than

\[
4\left(\frac{n}{n+1}\right)^4>1.
\tag{29}
\]

Hence `4^n L_n` is increasing for `n>=9`. From (22) and (25),

\[
L_n>\frac2{4^n}>\delta_n
\qquad(n\ge9).
\tag{30}
\]

Combining (21), (22), and (30), with the trivial `|t|<=1/4` case, proves (3).

## 4. Consequence and boundary

The accepted moment route had two unbounded quantifiers, over `n` and `t`. The present result removes the moment-order noncompactness while **simultaneously controlling all real frequencies**. In particular, a hypothetical large-order counterexample cannot escape by sending its minimizing horizontal frequency to infinity; the endpoint shell already prevents that.

What remains is finite: decide (2) for `n=2,...,8`. A violation at any one of those orders kills this sufficient all-moment route, but would not contradict the already certified five-point zero-freeness of `ANF-062`. Conversely, certifying those seven orders would complete the sufficient moment condition recorded in `CLUE-even-moment-radial-coercivity`, and its existing series bridge would then yield the proposed sharp five-point coercivity and radial monotonicity statement.

The proof is profile-specific through (7). It does not address larger conjugation-invariant multisets or imply RH.

## 5. Prior art and audit boundary

The ingredients are standard: endpoint comparison, beta normalization, elementary Fourier anti-concentration on one interval, and rational Taylor bounds. Endpoint/Laplace concentration and positive-definite bandlimited extremal methods are classical; no novelty is claimed for those tools. A targeted check of Montgomery--Taylor/extremal-function and endpoint-asymptotic literature did not identify the specific inequality (2) or cutoff (3). No external theorem is load-bearing here, so `SOURCES.md` is unchanged.

The decisive audit is short: recheck the exact density (5), the two-sided comparison (7), the interval identity (13), the scalar inequality (14), and the rational comparison (25). If those survive, every possible failure of the accepted all-moment route is confined to the seven orders in (4).