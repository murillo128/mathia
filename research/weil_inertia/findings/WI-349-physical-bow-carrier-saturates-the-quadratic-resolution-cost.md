# WI-349 — the physical bow carrier saturates the quadratic resolution cost

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + NON-RH`.

## Claim

WI-348 proves that a phase-sensitive bow feature with a uniform ordinary source modulus obeys a quadratic covering bound and hence, in the Lipschitz/nonvanishing specialization,

\[
\frac{L}{\mu}\gg \sqrt{r_\tau}.
\]

One possible escape is to object that WI-348 covers the two-parameter phase-saturated cylinder rather than the one-parameter **physical** carrier. That does not improve the exponent in the uniform class. The physical one-parameter carrier itself can have quadratic metric entropy at the resolution set by its absolute carrier frequency, and Kirszbraun extension turns that packing into a height-independent Lipschitz feature family with extensive Gram rank and sensitivity only of order the square root of that rank.

More precisely, take a two-point source support with logarithmic coordinates

\[
x_-<x_+,
\qquad
x_c:=\frac{x_-+x_+}{2},
\qquad
\Delta:=x_+-x_->0,
\qquad
R:=\frac{x_c}{\Delta}.
\tag{1}
\]

Give the two coordinates equal normalized weights and put

\[
H:=\Delta^{-1}.
\tag{2}
\]

Thus the bow aperture is exactly

\[
H\Delta=1.
\tag{3}
\]

For any height interval of width `H`, write the physical carrier after translating the left endpoint to zero as

\[
w(t)
=
\frac1{\sqrt2}
\left(
 e^{it(R-1/2)},
 e^{it(R+1/2)}
\right),
\qquad 0\le t\le1,
\tag{4}
\]

where `t=\Delta(U-U_0)`. Assume `R\ge4\pi` and set

\[
n:=\left\lfloor\frac{R}{2\pi}\right\rfloor\ge2.
\tag{5}
\]

Then the actual one-parameter orbit contains `n^2` points whose pairwise Hilbert distances are strictly larger than `2/R`. Consequently, if

\[
\rho:=R^{-1}=\frac{\Delta}{x_c},
\tag{6}
\]

then its ordinary Hilbert covering number satisfies

\[
\boxed{
N_{\rm phys}(\rho)
\ge n^2
\ge \frac{R^2}{16\pi^2}
=
\frac1{16\pi^2\rho^2}.
}
\tag{7}
\]

Thus the `O(\rho^{-2})` exponent in WI-348 cannot be improved uniformly to `O(\rho^{-1})` merely by replacing the phase-saturated cylinder by the physical one-dimensional path.

The obstruction is stronger than a covering-method artifact. There exists a height-independent feature map on the whole source Hilbert space satisfying

\[
\|F(x)-F(y)\|\le L\|x-y\|,
\qquad
\|F(x)\|\ge1,
\qquad
L\le\frac{R}{\sqrt2},
\tag{8}
\]

such that on these `M=n^2` sampled physical heights the normalized output Gram matrix is

\[
G=\frac12(I_M+J_M).
\tag{9}
\]

Its spectrum is

\[
\frac{M+1}{2},
\quad
\underbrace{\frac12,\ldots,\frac12}_{M-1\text{ times}}.
\tag{10}
\]

Hence for every fixed `0<\tau<1/2`,

\[
\boxed{
r_\tau(G)\ge (1-2\tau)M
\ge
\frac{1-2\tau}{16\pi^2}R^2.
}
\tag{11}
\]

Together with (8), this realizes

\[
\frac{L}{\mu}=O(\sqrt{r_\tau})
\tag{12}
\]

inside the exact hypothesis class of WI-348. Therefore WI-348's square-root sensitivity/resolution law is optimal in exponent for arbitrary height-independent nonprojective Lipschitz feature maps. Any stronger universal theorem, such as a linear `L/\mu\gg r_\tau` law obtained only from one-dimensionality of the physical path, is false.

This is a barrier for the **generic feature-geometry route**, not for the zeta-specific bow problem. The extremizer deliberately uses only two source coordinates and an arbitrary Kirszbraun-extended feature map. Arithmetic restrictions on the actual `\Lambda-\Lambda^\sharp` source, additional covariance identities, phase equivariance, restricted feature algebras, or a theorem that exploits more than ordinary Lipschitz regularity can still produce stronger compression.

## 1. Exact distance law on the two-point physical carrier

For `s,t in [0,1]`, direct expansion of (4) gives

\[
\begin{aligned}
\langle w(t),w(s)\rangle
&=
 e^{iR(t-s)}\cos\frac{t-s}{2},\\
\|w(t)-w(s)\|^2
&=
2-2\cos(R(t-s))\cos\frac{t-s}{2}.
\end{aligned}
\tag{13}
\]

The large center frequency `R` therefore winds the ordinary phase rapidly while the centered coordinate changes only at unit scale. Projectively this phase disappears, which is why WI-347 has a one-dimensional `O(\rho^{-1})` cover. Ordinary phase-sensitive geometry retains it.

## 2. An explicit `n` by `n` packing on the one-dimensional path

For

\[
a,b\in\{0,1,\ldots,n-1\},
\]

set

\[
t_{a,b}
:=
\frac{2\pi}{R}
\left(a+\frac bn\right).
\tag{14}
\]

Because `R\ge2\pi n`,

\[
0\le t_{a,b}
\le
\frac{2\pi}{R}\left(n-\frac1n\right)
<1,
\tag{15}
\]

so all `n^2` points are on the physical height interval.

For two distinct pairs put

\[
A:=a-a',
\qquad
B:=b-b',
\qquad
\delta:=t_{a,b}-t_{a',b'}
=
\frac{2\pi}{R}\left(A+\frac Bn\right).
\tag{16}
\]

Then

\[
R\delta=2\pi A+\frac{2\pi B}{n}.
\tag{17}
\]

If `B=0`, then `A\ne0`; since every `t_{a,b}` lies in `[0,1)`, equation (13) and monotonicity of sine on the relevant range give

\[
\|w(t_{a,b})-w(t_{a',b})\|
=
2\sin\frac{|\delta|}{4}
\ge
2\sin\frac{\pi}{2R}.
\tag{18}
\]

If `B\ne0`, the phase in (17) is separated from a multiple of `2\pi` by at least `2\pi/n`. When its cosine is nonnegative, `\cos(\delta/2)\le1` gives

\[
\|w(t_{a,b})-w(t_{a',b'})\|
\ge2\sin\frac{\pi}{n};
\tag{19}
\]

when that cosine is negative, equation (13) gives squared distance greater than `2`, which is even stronger. Thus (18) is the smaller universal separation.

For `0<x<\pi/2`, strict concavity gives `\sin x>2x/\pi`. Taking `x=\pi/(2R)` yields

\[
2\sin\frac{\pi}{2R}>
\frac2R.
\tag{20}
\]

Therefore the `n^2` points are strictly `2/R`-separated. A closed Hilbert ball of radius `1/R` can contain at most one of them, proving the first inequality in (7).

Finally `R/(2\pi)\ge2`, so

\[
n=\left\lfloor\frac{R}{2\pi}\right\rfloor
\ge\frac{R}{4\pi},
\tag{21}
\]

which proves the second inequality in (7).

The packing uses the actual one-dimensional trajectory, not the phase-saturated superset from WI-348. The two indices have a transparent meaning: `a` chooses successive phase windings separated by a slow centered drift of order `1/R`, while `b` resolves `n` distinct positions around the phase circle inside each slow layer.

## 3. The construction is admissible for genuine integer source coordinates

No abstract non-arithmetic frequencies are required. Take for example

\[
x_-:=\log q,
\qquad
x_+:=\log(q+1)
\tag{22}
\]

for an integer `q`, with source coefficients supported only on `q` and `q+1`. Then

\[
\Delta=\log\left(1+\frac1q\right),
\qquad
x_c=\frac{\log q+\log(q+1)}2,
\tag{23}
\]

and

\[
R=\frac{x_c}{\Delta}\to\infty.
\tag{24}
\]

Indeed `\Delta<1/q` and `x_c>\log q`, so `R>q\log q`. Hence infinitely many genuine two-integer supports satisfy `R\ge4\pi` (already every sufficiently large `q` does). Translating the chosen height window by an arbitrary `U_0` applies a common diagonal unitary to all points and leaves every pairwise distance unchanged, so the construction is equally valid on a high zeta-height window.

This arithmetic admissibility matters for the falsification role: the quadratic packing is not an artifact of allowing fictitious real logarithmic frequencies.

## 4. Kirszbraun upgrades the packing to a sharp feature-rank example

Enumerate the packed physical points as

\[
x_1,\ldots,x_M,
\qquad M=n^2,
\tag{25}
\]

and let `e_1,...,e_M` be an orthonormal basis of a real Hilbert target. Define on the finite set

\[
f_0(x_j):=e_j.
\tag{26}
\]

For `i\ne j`, equations (20) and (25) give

\[
\frac{\|f_0(x_i)-f_0(x_j)\|}
     {\|x_i-x_j\|}
<
\frac{\sqrt2}{2/R}
=
\frac{R}{\sqrt2}.
\tag{27}
\]

Thus `f_0` is `R/\sqrt2`-Lipschitz. The Kirszbraun--Valentine extension theorem for Hilbert spaces extends it to a map `f` on the entire source Hilbert space with the same Lipschitz constant.

Now append a constant orthogonal coordinate:

\[
F(x):=(1,f(x)).
\tag{28}
\]

Then `F` is still `R/\sqrt2`-Lipschitz and `\|F(x)\|\ge1` everywhere. At each packed point,

\[
h_j
:=
\frac{F(x_j)}{\|F(x_j)\|}
=
\frac{(1,e_j)}{\sqrt2}.
\tag{29}
\]

Therefore

\[
\langle h_i,h_j\rangle
=
\begin{cases}
1,&i=j,\\
1/2,&i\ne j,
\end{cases}
\tag{30}
\]

which is exactly (9). Equation (10) follows from the spectrum of `J_M`.

For `r\ge1`, the spectral mass below the first `r` eigenvalues is

\[
\sum_{j>r}\lambda_j(G)=\frac{M-r}{2}.
\tag{31}
\]

If this is at most `\tau M`, then

\[
r\ge(1-2\tau)M,
\tag{32}
\]

proving (11).

This example uses no explicit height argument inside `F`: after the source geometry has encoded the physical phase winding, `F` is an ordinary height-independent map of the source vector. It also satisfies the nonvanishing hypothesis of WI-348 uniformly with `\mu=1`.

## 5. What is and is not sharp

For each **fixed** two-point support, the curve (4) is rectifiable and one-dimensional. As `\rho\to0` with `R` fixed, its covering number is eventually `O_R(\rho^{-1})`; there is no contradiction with ordinary Minkowski dimension one.

The Research Watch needs a uniform statement over source families whose center frequency grows. Here the relevant support parameter `R=x_c/\Delta` tends to infinity, and the resolution is chosen at the natural carrier scale `\rho=1/R`. At precisely that coupled limit, a one-dimensional curve has length of order `R` and therefore enough room for order `R^2` distinguishable points at scale `1/R`. Equations (14)--(21) exhibit them explicitly.

Accordingly:

- WI-347's **projective** `O(r^{-1})` resolution collapse is not challenged; quotienting global phase removes the fast winding.
- WI-348's **ordinary/nonprojective** `O(r^{-1/2})` resolution collapse is sharp in exponent under its current broad hypotheses.
- The sharpness is uniform-class sharpness. It does not assert that the actual `\Lambda-\Lambda^\sharp` source realizes the Kirszbraun feature, nor that generic nonlinear features are arithmetically meaningful.
- A stronger bow theorem must use extra structure absent from WI-348's hypotheses: arithmetic covariance, restrictions on the feature algebra, phase/gauge equivariance, a source-specific norm, or another invariant not reducible to ordinary uniform continuity/Lipschitz sensitivity.

Thus the tempting refinement

\[
\text{physical path is one-dimensional}
\quad\Longrightarrow\quad
N(\rho)=O(\rho^{-1})\text{ uniformly}
\quad\Longrightarrow\quad
L/\mu\gg r_\tau
\tag{33}
\]

is decisively false.

## 6. Prior art and novelty boundary

The generic ingredients are classical. Covering/packing numbers and epsilon-entropy go back to Kolmogorov--Tikhomirov; WI-348 already records the standard metric-entropy background. The Hilbert-space Lipschitz extension step is the classical Kirszbraun--Valentine theorem. A modern explicit-formula reference is:

- Daniel Azagra, Erwan Le Gruyer and Carlos Mudarra, **Kirszbraun's Theorem via an Explicit Formula**, *Canadian Mathematical Bulletin* 64:1 (2021), 101--107, DOI `10.4153/S000843952000004X`. The theorem states that a Lipschitz map from a subset of one Hilbert space to another admits an extension with the same Lipschitz constant.

The external prior-art search also checked generic metric-entropy/packing and high-winding/Kronecker-flow terminology. It located the classical frameworks, but no result that changes the elementary calculation above or a zeta/bow-specific statement equivalent to (7)--(12). No external priority claim is made.

The line-local novelty audit is sharper. WI-347 proves a projective `O(\rho^{-1})` compression theorem and explicitly leaves essential global phase outside its hypotheses. WI-348 closes smooth global-phase sensitivity by phase-saturating the source, obtaining an `O(\rho^{-2})` input cover and an `L/\mu\gg\sqrt{r_\tau}` conditioning cost. It notes that the physical phase can wind arbitrarily often, but does not establish whether the quadratic exponent is necessary after restricting back to the physical path. The present finding supplies that missing lower-bound direction and a matching feature-rank construction: the physical path itself attains quadratic entropy at carrier-scale resolution, and an admissible Lipschitz feature realizes extensive rank with `L/\mu=O(\sqrt r)`.

## Research consequence

Do not spend further effort trying to strengthen WI-348 from square-root to linear resolution cost solely by observing that the physical carrier is a one-dimensional path. That route is closed under WI-348's broad arbitrary-feature hypotheses.

The accepted distinguished-twist clue remains unresolved. This finding does not estimate the signed `\Lambda-\Lambda^\sharp` off-diagonal covariance and does not answer its decisive test. It instead narrows the generic-feature escape hatch one step further: any stronger compression must import genuinely source-specific arithmetic or structural restrictions beyond ordinary phase-sensitive Lipschitz geometry.