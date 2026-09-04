# ANF-036 — four-point complex tests collapse to real multiplicities, and five points are sharp

**Status:** `EXACT-DERIVED + COMPLEX-FALSIFIER-BOUNDARY + SHARP-CARDINALITY-THRESHOLD`. `ANF-035` shows that a common symmetric vertical fiber over an arbitrary real base is never more dangerous than collapsing that fiber onto the real axis once the compact-band spectrum satisfies `J>=0`. Its stated next test was the smallest configuration with genuine horizontal--vertical coupling, beginning with `{0,x+iy,x-iy}`. That candidate still does not escape. In fact **every conjugation-invariant multiset of total cardinality at most four is dominated by its real-part collapse**. This cardinality threshold is sharp from spectral positivity alone: at five points there are explicit conjugation-invariant configurations and continuous even `J>=0` for which vertical displacement strictly *lowers* the pair energy.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\tag{1}
\]

where `J` is real and even. For a finite conjugation-invariant multiset `W`, write

\[
E_F(W)=\sum_{z,w\in W}F(z-w)
=\int_{-B}^{B}J(\alpha)|S_W(\alpha)|^2\,d\alpha,
\qquad
S_W(\alpha)=\sum_{w\in W}e^{-2\pi i\alpha w}.
\tag{2}
\]

Define the **real-part collapse** `R(W)` by replacing every entry `w` of `W`, with multiplicity, by `Re(w)`. Then for every conjugation-invariant `W` with

\[
|W|\le4,
\]

one has

\[
\boxed{
E_F(W)\ge E_F(R(W)).
}
\tag{3}
\]

Moreover

\[
\boxed{
s(W)\ge s(R(W)),
}
\tag{4}
\]

because collapsing a nonreal conjugate pair creates a real point of multiplicity at least two and can only destroy, never create, simple real points. Consequently any universal affine inequality

\[
s(Z)\ge A|Z|-tE_F(Z),
\qquad t>0,
\tag{5}
\]

that holds for the real multiset `R(W)` automatically holds for `W`. Thus **no complex configuration of size at most four contributes a genuinely new affine constraint beyond real multiplicity tests**.

The bound `4` cannot be improved using only `J>=0`. There is a five-point conjugation-invariant multiset `W` and a continuous even nonnegative compact-band spectrum `J` for which

\[
\boxed{
E_F(W)<E_F(R(W)).
}
\tag{6}
\]

Hence five points are the first cardinality at which horizontal--vertical coupling can genuinely beat the corresponding real collapse.

## 1. One conjugate pair plus at most two real points always collapses

Suppose first that `W` has exactly one nonreal horizontal fiber. Thus a conjugate pair

\[
x+iy,\qquad x-iy,
\qquad y>0,
\]

appears with the same multiplicity `k>=1`, and all remaining entries are real. Since `|W|<=4`, if `r` is the number of remaining real entries counted with multiplicity, then

\[
2k+r\le4.
\tag{7}
\]

For fixed real frequency `alpha`, put

\[
c:=\cosh(2\pi\alpha y)\ge1,
\qquad
z:=e^{-2\pi i\alpha x},
\qquad |z|=1,
\tag{8}
\]

and let

\[
A:=\sum_{u\in W\cap\mathbb R}e^{-2\pi i\alpha u},
\tag{9}
\]

with real multiplicities. Then

\[
S_W=A+2kc z,
\qquad
S_{R(W)}=A+2kz.
\tag{10}
\]

A direct expansion gives

\[
\begin{aligned}
|S_W|^2-|S_{R(W)}|^2
&=4k^2(c^2-1)+4k(c-1)\Re(A\bar z)\\
&=\boxed{
4k(c-1)\bigl(k(c+1)+\Re(A\bar z)\bigr).
}
\end{aligned}
\tag{11}
\]

Because `A` is a sum of `r` unit complex numbers,

\[
\Re(A\bar z)\ge-|A|\ge-r.
\tag{12}
\]

Therefore

\[
k(c+1)+\Re(A\bar z)
\ge k(c+1)-r
\ge2k-r.
\tag{13}
\]

The cardinality condition (7) forces `r<=4-2k`, hence

\[
2k-r\ge4k-4.
\tag{14}
\]

For `k=1`, this is nonnegative because `r<=2`; for `k=2`, necessarily `r=0` and it is strictly positive away from `alpha y=0`. Larger `k` cannot occur when `|W|<=4`. Thus (11) is pointwise nonnegative for every `alpha`.

This proves (3) for every configuration consisting of one conjugate pair together with zero, one, or two real points. In particular the three-point test proposed at the end of `ANF-035`,

\[
\{0,x+iy,x-iy\},
\tag{15}
\]

is always dominated by

\[
\{0,x,x\}.
\tag{16}
\]

Indeed in that case `r=k=1`, and (11) reduces to

\[
4(c-1)\bigl(c+1+\cos(2\pi\alpha x)\bigr)
\ge4c(c-1)\ge0.
\tag{17}
\]

The same argument covers the four-point mixed case with two real entries and one conjugate pair. No choice of their horizontal phases can overcome the factor `c+1>=2`, because two real unit phases have total projection at least `-2`.

## 2. Two conjugate pairs at different heights also collapse

The remaining genuinely complex four-point geometry consists of two conjugate pairs, possibly at different horizontal positions and different heights:

\[
x_1\pm iy_1,
\qquad
x_2\pm iy_2,
\qquad y_1,y_2>0.
\tag{18}
\]

Set

\[
c_j:=\cosh(2\pi\alpha y_j)\ge1,
\qquad
z_j:=e^{-2\pi i\alpha x_j},
\tag{19}
\]

so that

\[
S_W=2(c_1z_1+c_2z_2),
\qquad
S_{R(W)}=2(z_1+z_2).
\tag{20}
\]

Writing

\[
\theta:=2\pi\alpha(x_1-x_2),
\]

a second direct expansion gives

\[
\frac14\bigl(|S_W|^2-|S_{R(W)}|^2\bigr)
=c_1^2+c_2^2-2+2(c_1c_2-1)\cos\theta.
\tag{21}
\]

Since `c_1c_2-1>=0`, the right side is minimized at `cos theta=-1`. At that endpoint it becomes

\[
c_1^2+c_2^2-2-2(c_1c_2-1)
=(c_1-c_2)^2\ge0.
\tag{22}
\]

Hence

\[
|S_W(\alpha)|^2\ge|S_{R(W)}(\alpha)|^2
\qquad\text{for every real }\alpha.
\tag{23}
\]

This is stronger than an integrated positive-spectrum statement. Even when the two pairs have different heights, the worst horizontal destructive interference cannot make the vertically displaced four-point structure factor smaller than the doubled-real collapse.

Together with Section 1 and the trivial all-real case, (23) exhausts every conjugation-invariant multiset of cardinality at most four and proves the pointwise form of (3).

## 3. Affine counting consequence

Equation (3) follows by integrating the pointwise structure-factor inequality against `J>=0`. The simple-point comparison (4) is equally direct. A nonreal conjugate pair contributes no real simple points before collapse and becomes at least a double real point afterward. If its real part coincides with an existing real point, that existing point may cease to be simple; no operation can move in the opposite direction.

Therefore, if the real collapse satisfies (5), then

\[
\begin{aligned}
s(W)
&\ge s(R(W))\\
&\ge A|R(W)|-tE_F(R(W))\\
&\ge A|W|-tE_F(W),
\end{aligned}
\tag{24}
\]

because `|R(W)|=|W|` and `t>0`. This establishes the exact affine-dominance statement.

For the post-`ANF-034` program the consequence is concrete. The first complex test not reducible by spectral positivity to a real multiset does **not** occur at a single conjugate pair plus a real anchor, nor at two conjugate pairs with unequal heights. All two-, three-, and four-point conjugation-invariant tests are already part of the real-multiplicity problem after collapse.

This does not mean that the central-notch separator of `ANF-034` has already passed every real multiset of size at most four; it says that any failure at those cardinalities is a **real-multiplicity failure**, not a new complex-geometric one. The distinction matters because the finite-real separation in `ANF-034` is formulated for distinct real sets, while the affine envelope also contains multiplicity constraints from `ANF-005` and `ANF-017`.

## 4. Five points are the first possible nontrivial complex layer

The preceding argument is sharp. Fix any

\[
0<\alpha_0<B
\tag{25}
\]

and choose `y>0` so that

\[
1<c_0:=\cosh(2\pi\alpha_0 y)<2.
\tag{26}
\]

Take the conjugate pair at horizontal coordinate zero,

\[
iy,-iy,
\]

and three distinct real points

\[
r_j:=\frac{2j-1}{2\alpha_0},
\qquad j=1,2,3.
\tag{27}
\]

At frequency `alpha_0`, all three real phases equal `-1`:

\[
e^{-2\pi i\alpha_0 r_j}=-1.
\tag{28}
\]

Thus in the notation of Section 1, `k=1`, `z=1`, `A=-3`, and equation (11) gives

\[
\boxed{
|S_W(\alpha_0)|^2-|S_{R(W)}(\alpha_0)|^2
=4(c_0-1)(c_0-2)<0.
}
\tag{29}
\]

The same strict inequality holds at `-alpha_0`, and by continuity it persists on symmetric neighborhoods of `+/-alpha_0`. Choose any nonzero continuous even `J>=0` supported inside those neighborhoods. Then (2) and (29) imply

\[
E_F(W)-E_F(R(W))<0,
\tag{30}
\]

which proves (6).

The simple-point count is unchanged in this example provided the three `r_j` are distinct from zero: `W` has exactly three simple real points, and `R(W)` has the same three simple points plus a double point at zero. Hence the energy reversal is not hidden by bookkeeping. For a fixed affine amplitude `t>0`, the five-point complex configuration gives a strictly stronger right-hand side than its real collapse.

This is an existence statement for the positive-spectrum class, not a claim that the specific central-notch spectrum `J_s` from `ANF-034` realizes the reversal. Its role is sharper: **no argument using only `J>=0` can push the real-collapse theorem beyond four points.** Any further reduction must exploit the actual shape of `J_s`, the compulsory slack from `ANF-005`, or additional structure of the affine certificate.

## 5. Structural interpretation

The threshold has a simple phase-budget explanation. Moving one conjugate pair off the real axis replaces its real-collision amplitude `2` by

\[
2\cosh(2\pi\alpha y)>2.
\]

Against at most two remaining real unit phases, this increased amplitude cannot make the total structure factor smaller: the opposing real projection is bounded below by `-2`. Three independent real phases are the first time the horizontal part can contribute projection `-3`; then a modest vertical amplification with `1<c<2` can move the pair amplitude *toward* cancellation rather than away from it.

Two conjugate pairs at four points behave differently because both amplitudes are amplified. Their worst relative phase is `pi`, and the residual difference is exactly the square `(c_1-c_2)^2`. The first imbalance capable of exploiting one amplified fiber against enough unamplified horizontal mass therefore appears at total cardinality five.

This identifies a more precise notion of the horizontal--vertical coupling left open by `ANF-035`. Heterogeneous heights by themselves are not enough. What matters is an **amplitude imbalance between vertical fibers and at least three independent real-phase units, or an equivalent five-point coupling pattern**.

## 6. Prior art and evidence boundary

The load-bearing analytic representation is already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides and in `ANF-012`: a positive compact-band spectrum turns pair energy into the integral of `J|S_W|^2`. The new statements are the finite-cardinality inequalities (11)--(23) and the sharp five-point construction (25)--(30), all elementary consequences of that representation.

A targeted literature search of complex positive-definite strip functions and Fourier--Laplace representations found the expected classical representation theory but no theorem matching this particular real-part-collapse threshold for conjugation-invariant finite multisets. No publication-level novelty claim is made. The result is persisted because it gives an exact and reusable falsification boundary inside the Mathia affine-certificate reduction.

No additional source entry is required: the external theorem used here is the same Fourier--Laplace/positive-spectrum framework already recorded for `ANF-012` and `ANF-035`.

The theorem does not establish a better unconditional zeta-zero proportion, does not prove that all real multiplicity tests are harmless, and does not show that a five-point configuration kills `J_s`. It only locates the first cardinality where genuinely complex geometry can add information once spectral positivity is imposed.

## 7. Next decisive test

The cheapest post-`ANF-035` complex audit is now a five-point one. Start with three real points and one conjugate pair,

\[
\{r_1,r_2,r_3,x+iy,x-iy\},
\tag{31}
\]

because equation (11) gives its exact deviation from the real collapse:

\[
4(c-1)\left(c+1+\Re\left(Ae^{2\pi i\alpha x}\right)\right).
\tag{32}
\]

For the explicit central-notch ray `J_s`, integrate (32) against the actual `J_s`, combine it with the exact simple/multiplicity envelope and normalization slack from `ANF-005`/`ANF-017`, and ask whether any choice of the three real phases and `y` consumes the strict finite-real gain of `ANF-034`.

If every such five-point test can still be dominated using the special shape of `J_s`, the next obstruction must use more global complex coupling. If a five-point witness already beats the ray, the universal affine scalar branch closes at the first cardinality where positive-spectrum geometry permits a genuinely new complex constraint.