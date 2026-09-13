# NB-084 — integer-descendant prediction is governed by an aliased boundary spectrum

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + INTEGER-DESCENDANT-PREDICTION + TOEPLITZ-PERIODIZATION + RADIAL-SCREENING-CERTIFICATE + ALIASING-BOUNDARY + METHOD-ADVANCE`.

`NB-081`--`NB-083` calibrate finite-depth screening on stationary branch filters and show that qualitative outerness is not enough: for the polynomial control `1-z`, a boundary zero leaves an anchored finite-prediction excess of order `1/L`, so bounded prediction-volume charge needs descendant depth of order `R`. The live question is whether the actual nonstationary Nyman innovations inherit an analogous boundary-zero penalty or have a quantitatively better inverse-prediction channel.

The exact integer branching of the actual source supplies a first source-specific answer. Fix an innovation

\[
D_j=(j+1)F_{j+1}-jF_j,
\]

an integer dilation `q>=2`, and write `h=log q`. For `L>=1` define the **radial descendant prediction error**

\[
\boxed{
\mathcal E_{j,q,L}
:=
\inf_{a_1,\ldots,a_L}
\left\|
D_j+\sum_{r=1}^L a_rU_{rh}D_j
\right\|^2.
}
\tag{1}
\]

Exact branching makes every predictor in (1) an admissible linear combination of actual later innovations. Consequently, for the depth-`L` horizon

\[
N_{R,L}^{(q)}=q^LR-1,
\]

one has for every `j<R`

\[
\boxed{
\Pi_{j,N_{R,L}^{(q)}}^2
\le
\mathcal E_{j,q,L}.
}
\tag{2}
\]

The important point is that (1) is not controlled by the unperiodized half-plane boundary factor. Its exact scalar spectral density is the **aliased periodization**

\[
\boxed{
W_{j,q}(\theta)
:=
\frac1h
\sum_{k\in\mathbb Z}
\left|
D_j\!\left(\frac12+i\frac{\theta+2\pi k}{h}\right)
\right|^2,
\qquad -\pi\le\theta<\pi,
}
\tag{3}
\]

with equality in `L^1(T)` and almost everywhere. If

\[
p(z)=1+\sum_{r=1}^La_rz^r,
\]

then Paley--Wiener/Parseval gives the exact anchored Toeplitz problem

\[
\boxed{
\mathcal E_{j,q,L}
=
\inf_{\substack{p(0)=1\\\deg p\le L}}
\frac1{2\pi}
\int_{-\pi}^{\pi}
W_{j,q}(\theta)|p(e^{-i\theta})|^2\,d\theta.
}
\tag{4}
\]

Equivalently, if

\[
T_{j,q,L}
=
\left(
\langle U_{rh}D_j,U_{sh}D_j\rangle
\right)_{0\le r,s\le L},
\]

then

\[
\boxed{
\mathcal E_{j,q,L}
=
\frac1{(T_{j,q,L}^{-1})_{00}}.
}
\tag{5}
\]

Thus the actual source does have an exact finite-prediction scalar, analogous in role to `a_(psi,L)` in `NB-082`, but it is **nonstationary in `j` and already contains frequency aliasing before any estimate is made**.

This changes the boundary-zero calibration materially. A zero of one continuous boundary sample removes only one summand in (3). To force

\[
W_{j,q}(\theta)=0,
\]

all frequencies in the complete alias class

\[
\frac{\theta+2\pi k}{\log q},
\qquad k\in\mathbb Z,
\tag{6}
\]

must simultaneously be boundary zeros of `D_j` (at points where the boundary values are defined). In particular, isolated critical-line zeros of the zeta factor do **not** by themselves become unit-circle zeros of the prediction density. The `1/L` boundary-zero law of `NB-083` therefore cannot be transferred to the actual Nyman source merely by observing that the continuous Mellin factor has critical-line zeros.

Moreover,

\[
\boxed{W_{j,q}(\theta)>0\quad\text{for almost every }\theta.}
\tag{7}
\]

Indeed, `D_j` is a nonzero half-plane `H^2` vector, so its boundary function is nonzero almost everywhere; the `k=0` summand in (3) already proves (7). This is only a qualitative fact. It does **not** imply a useful finite prediction rate: the periodized density may have arbitrarily deep valleys, and (4) may still converge too slowly for the `1/R` scale required by `NB-082`-type volume screening.

The useful source-facing consequence is instead the finite certificate

\[
\boxed{
\mathfrak J_{R,q^LR-1}
\le
\sum_{j=1}^{R-1}
\log
\frac{\mathcal E_{j,q,L}}
{\widehat\Pi_{j,R}^2}
\le
\sum_{j=1}^{R-1}
\log
\frac{\mathcal E_{j,q,L}}
{\|C_j\|^2}.
}
\tag{8}
\]

Hence an unbounded sequence of pairs `(R,L(R))` for which either right-hand side stays bounded rules out the stable tail by `NB-074`. The live arithmetic target is now precise: control the anchored Toeplitz prediction errors of the **periodized Nyman spectra** (3), relative to the visible causal innovations, strongly enough that their aggregate excess is `O(1)`.

## 1. Exact branching turns dilation shifts into admissible future predictors

`NB-069` gives for every integer `q>=2`

\[
U_{\log q}D_j
=
q^{-1/2}
\sum_{k=qj}^{q(j+1)-1}D_k.
\tag{9}
\]

Iterating,

\[
\boxed{
U_{r\log q}D_j
=
q^{-r/2}
\sum_{k=q^rj}^{q^r(j+1)-1}D_k
\qquad(r\ge1).
}
\tag{10}
\]

Every index on the right is strictly larger than `j`. If `j<R` and `r<=L`, then

\[
q^r(j+1)-1
\le
q^LR-1.
\tag{11}
\]

Therefore all the shifted vectors used in (1) belong to

\[
\operatorname{span}\{D_{j+1},\ldots,D_{q^LR-1}\}.
\]

The global finite-future prediction error `Pi_(j,N)` minimizes over that complete future span, so (2) follows immediately.

This is the point at which the calculation becomes source-specific. For an arbitrary causal family, future copies of one innovation need not exist. Here they are exact block averages of actual descendants, with no approximation, Gram inversion, or target oracle.

## 2. Fiberizing one integer-dilation ray gives the periodized spectrum

On the critical boundary, the shift satisfies

\[
(U_hG)\!\left(\frac12+it\right)
=e^{-iht}G\!\left(\frac12+it\right).
\tag{12}
\]

Hence

\[
\left\|
D_j+\sum_{r=1}^La_rU_{rh}D_j
\right\|^2
=
\frac1{2\pi}
\int_{\mathbb R}
\left|
D_j\!\left(\frac12+it\right)
\right|^2
\left|p(e^{-iht})\right|^2dt.
\tag{13}
\]

Split the real line into the alias intervals

\[
ht\in[-\pi+2\pi k,\pi+2\pi k),
\qquad k\in\mathbb Z,
\]

and set `theta=ht-2pi k`. Since `p(e^{-i(theta+2pi k)})=p(e^{-itheta})`, (13) becomes

\[
\frac1{2\pi}
\int_{-\pi}^{\pi}
W_{j,q}(\theta)|p(e^{-i\theta})|^2d\theta,
\tag{14}
\]

which proves (3)--(4). Tonelli applies because every summand is nonnegative and `D_j in H^2`, so

\[
\frac1{2\pi}
\int_{-\pi}^{\pi}W_{j,q}(\theta)d\theta
=\|D_j\|^2<\infty.
\tag{15}
\]

The Fourier coefficients of `W_(j,q)` are exactly

\[
\widehat W_{j,q}(r-s)
=
\langle U_{rh}D_j,U_{sh}D_j\rangle,
\tag{16}
\]

so the Gram matrix of the radial shifts is the Toeplitz matrix `T_(j,q,L)`. The vectors are finitely independent: `D_j` has nonzero first-cell component, while the positive shifts have strictly later left support endpoints. Thus `T_(j,q,L)>0`. Standard constrained quadratic minimization with the coefficient of `z^0` fixed to one gives (5).

No stationarity of the full Nyman family is being asserted. Stationarity appears only after restricting to the exact dilation ray of one fixed innovation. The dependence on `j` remains inside the spectral density (3).

## 3. Aliasing is the correct boundary test, not the continuous Mellin zero set

From the explicit source formula,

\[
D_j(s)
=
O(s)
\frac{j^{1-s}-(j+1)^{1-s}}{s-1}
=
\frac{\zeta(s)}{sB(s)}
\bigl(j^{1-s}-(j+1)^{1-s}\bigr).
\tag{17}
\]

On `Re s=1/2`, the last factor cannot vanish: its two terms have moduli `sqrt(j)` and `sqrt(j+1)`. Thus, wherever the Blaschke boundary value is regular, the only arithmetic vanishing comes from the zeta factor. But (3) does not use one boundary value; it sums the squared modulus over the whole congruence class modulo `2pi/h` in frequency.

Because all summands are nonnegative,

\[
W_{j,q}(\theta)=0
\quad\Longrightarrow\quad
D_j\!\left(
\frac12+i\frac{\theta+2\pi k}{h}
\right)=0
\quad\text{for every }k\in\mathbb Z
\tag{18}
\]

at points where these boundary values are defined. Thus one critical-line zero can suppress one alias but cannot by itself create the unit-circle boundary zero that drove `NB-083`. A genuine zero of (3) would require an entire two-sided arithmetic progression of aliased boundary zeros with spacing

\[
\frac{2\pi}{\log q}.
\tag{19}
\]

No claim is made here that such a progression is impossible. It is simply a much stronger and different condition than the existence of ordinary critical-line zeros.

The almost-everywhere statement (7) is easier and unconditional. A nonzero Hardy function cannot have boundary value zero on a set of positive measure. Therefore

\[
\left|D_j\!\left(\frac12+i\frac\theta h\right)\right|>0
\]

for almost every `theta`, and the single `k=0` term makes `W_(j,q)>0` there.

This distinction is important for the live method. `NB-083` shows that a genuine unit-circle zero of a stationary prediction symbol can force reciprocal-depth screening. Equation (3) shows that the relevant symbol extracted from the actual integer-dilation descendants is **not** the continuous factor `O` or `zeta/B`; it is their alias-periodized energy after multiplication by the shrinking-cell innovation factor. Boundary-zero heuristics must therefore be applied to `W_(j,q)`, not to the unaliased Mellin factor.

## 4. The radial Toeplitz errors give an actual-source stable-tail certificate

`NB-074` gives

\[
\mathfrak J_{R,N}
=
\sum_{j<R}
\log
\frac{\Pi_{j,N}^2}{\widehat\Pi_{j,R}^2},
\qquad
\Pi_{j,N}^2\ge\widehat\Pi_{j,R}^2.
\tag{20}
\]

Using (2) term by term at `N=q^LR-1` yields the first inequality in (8). `NB-074` also gives

\[
\widehat\Pi_{j,R}^2\ge\|C_j\|^2>0,
\tag{21}
\]

which gives the second.

Define the source-visible radial excess

\[
\boxed{
\alpha_{j,q,L;R}
:=
\frac{\mathcal E_{j,q,L}}
{\widehat\Pi_{j,R}^2}-1
\ge0.
}
\tag{22}
\]

Then

\[
\boxed{
\mathfrak J_{R,q^LR-1}
\le
\sum_{j<R}\log(1+\alpha_{j,q,L;R}).
}
\tag{23}
\]

This is the actual-source analogue of the stationary comparison `mathfrak J asymp R a_(psi,L)` in `NB-082`, but without pretending that all innovations share one scalar filter. If the average excess is of order `1/R`, the total charge is bounded; if the sum tends to zero, the finite certificate itself tends to the flat value.

The criterion is only sufficient. The full future can predict better than the radial descendant shifts, so large `mathcal E_(j,q,L)` does not imply a stable tail. Conversely, a useful upper bound on (23) immediately rules the stable tail out. This one-sided direction is exactly the one needed for a source proof.

## 5. Controls and falsification boundary

For the flat control `O=1`, `NB-062` gives

\[
D_j^{(0)}(t)=e^{t/2}\mathbf1_{[\log j,\log(j+1)]}(t),
\qquad
\|D_j^{(0)}\|=1.
\tag{24}
\]

Since

\[
\log\frac{j+1}{j}\le\log2\le\log q,
\]

the shifted vectors `U_(r log q)D_j^(0)` have disjoint supports. Hence

\[
W_{j,q}^{(0)}(\theta)=1
\quad\text{a.e.},
\qquad
\mathcal E_{j,q,L}^{(0)}=1,
\qquad
\widehat\Pi_{j,R}^{(0)}=1,
\tag{25}
\]

and (23) gives the exact zero charge. The certificate therefore does not manufacture a false boundary layer in the memory-free model.

At the opposite extreme, (7) is deliberately not promoted to a quantitative screening theorem. A positive almost-everywhere spectral density can approach zero arbitrarily rapidly on thin sets, and finite Toeplitz prediction can remain badly conditioned. The new quantity has been identified exactly; its rate has not been estimated.

Likewise, (18) does not exclude an aliased zero progression of the actual boundary function, nor does it prove any spacing theorem for zeta zeros. The finding only shows that **ordinary individual critical zeros are not the correct stationary boundary singularities after integer-dilation fiberization**. Any future use of zero spacing must be separately proved and cannot be smuggled in through generic folklore.

Finally, the radial family is only a subfamily of the complete future innovations. This is an advantage for the upper certificate (2), but it means failure of the radial bound cannot refute other screening mechanisms. The full nonstationary future may exploit cross-ray combinations invisible to one Toeplitz fiber.

## 6. Prior-art and consequence for the live frontier

Periodized Fourier energy and Toeplitz Gram matrices for integer translates are classical objects in the theory of principal shift-invariant spaces and prediction. For example, the standard periodization criterion for integer translates appears in the shift-invariant literature; Sandra Saliani's 2013 work on `l^2`-linear independence explicitly uses the corresponding periodization function, and the broader shift-invariant framework is classical. No novelty is claimed for fiberization, periodization, Toeplitz quadratic minimization, or Hardy boundary uniqueness.

A targeted search of Nyman--Beurling/Baez--Duarte literature located the classical semigroup formulation, recent Gram/block-compressibility work, and the existing Hardy orthogonality literature, but did not locate the specific conjunction used here: exact integer branching of the canonical causal innovations, restriction to one descendant ray, the alias-periodized boundary density (3), and its insertion as the finite upper certificate (8) for the renormalized stable-tail prediction volume. No priority claim is made.

No specialized external estimate is load-bearing: (2)--(5) are direct branching, Parseval, and finite quadratic minimization, while (7) uses only standard Hardy uniqueness. `SOURCES.md` therefore remains unchanged.

The frontier after `NB-083` is now narrower. The actual nonstationary inverse-prediction quantity is not an abstract analogue of the stationary filter and not the raw boundary modulus of `O`. One explicit sufficient channel is

\[
\boxed{
W_{j,q}
\longrightarrow
T_{j,q,L}
\longrightarrow
\mathcal E_{j,q,L}
\longrightarrow
\sum_{j<R}
\log\frac{\mathcal E_{j,q,L}}{\widehat\Pi_{j,R}^2}.
}
\tag{26}
\]

A useful next theorem should bound this aggregate at an affordable depth `L=L(R)`, perhaps by proving quantitative lower regularity for the aliased densities or by exploiting cancellation across `j`. What is no longer justified is to import the reciprocal-depth boundary-zero calibration of `NB-083` directly from individual critical-line zeros of the continuous zeta factor. Integer branching aliases the boundary spectrum first.