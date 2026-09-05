# ANF-060 — height-balance splice makes the Montgomery--Taylor five-point zero box explicit

**Status:** `EXACT-DERIVED + PROFILE-SPECIFIC-COMPACTIFICATION + RATIONAL-HYPERBOLIC-CERTIFICATE + MACHINE-READY-BOUNDARY`. `ANF-057` and `ANF-059` already force every genuine zero or negative value of the fixed Montgomery--Taylor two-pair defect away from the equal-height diagonal and into a narrow relative-separation interval. `ANF-049` supplies an independent scale-free height-balance exclusion but leaves it in implicit hyperbolic form. Intersecting the three exact restrictions gives a fully explicit absolute height ceiling:

\[
\boxed{
H_{\rm MT}(y_1,y_2;t_1,t_2)\le0
\quad\Longrightarrow\quad
0.545<|d|<1.01,
\qquad
q>0.1409,
\qquad
\frac{y_1+y_2}{|d|}<1.4855,
}
\tag{1}
\]

where

\[
d=t_1-t_2,
\qquad
q=\frac{|y_1-y_2|}{y_1+y_2}.
\tag{2}
\]

In particular,

\[
\boxed{
y_1+y_2<1.500355,\qquad
\frac{y_1+y_2}{2}<0.7501775.}
\tag{3}
\]

Thus the accepted Montgomery--Taylor base-zero problem no longer needs an unspecified large-height compactification. Before common-translation coherence is treated, every possible zero already lies in an explicit low-height shape box whose constants are rationally certified from the existing exact gates.

## 1. Intersect the strict mismatch and separation gates

For the exact Montgomery--Taylor profile, `ANF-057` proves

\[
H_{\rm MT}\le0
\quad\Longrightarrow\quad
q>0.1409.
\tag{4}
\]

The same strict implication follows for a zero because `ANF-057` proves `H_{\rm MT}>0` throughout `q\le0.1409`.

Independently, `ANF-059` proves

\[
H_{\rm MT}\le0
\quad\Longrightarrow\quad
0.545<|d|<1.01,
\tag{5}
\]

again with strict positivity outside the displayed annulus. These two restrictions are profile-specific and require no bounded-height hypothesis.

`ANF-049` gives the complementary scale-free safety splice. Put

\[
S:=\frac{y_1+y_2}{|d|}>0.
\tag{6}
\]

For unequal heights its amplitude mismatch at the splice frequency `alpha_d=1/(3|d|)` is

\[
\mathcal A(S,q)
:=2\sinh\!\left(\frac{\pi S}{3}\right)
\sinh\!\left(\frac{\pi qS}{3}\right).
\tag{7}
\]

If `mathcal A>=1`, the low-frequency phase guard and high-frequency amplitude guard cover the entire frequency axis and give `H_J>=0` for every nonnegative spectrum. For the present zero-exclusion argument we use a strict value `mathcal A>1`, which makes the high-frequency guard strict on an open frequency interval for `J_MT` and hence gives `H_MT>0`.

## 2. A rational certificate gives `S<1.4855`

The function `mathcal A(S,q)` is strictly increasing in both positive variables. By (4), every residual zero has `q>1409/10000`. We now prove that `S>=2971/2000=1.4855` is impossible.

Use the elementary rational lower bound

\[
\pi>\frac{314159}{100000}
\tag{8}
\]

and, for `x>0`, the positive Taylor truncation

\[
\sinh x>
 x+\frac{x^3}{6}+\frac{x^5}{120}+\frac{x^7}{5040}.
\tag{9}
\]

At the rational corner

\[
S_0=\frac{2971}{2000},
\qquad
q_0=\frac{1409}{10000},
\tag{10}
\]

set

\[
x_0=\frac{314159}{100000}\frac{S_0}{3}
=\frac{933366389}{600000000},
\qquad
z_0=q_0x_0
=\frac{1315113242101}{6000000000000}.
\tag{11}
\]

Exact rational evaluation of the right side of (9) gives

\[
2\left(x_0+\frac{x_0^3}{6}+\frac{x_0^5}{120}+\frac{x_0^7}{5040}\right)
\left(z_0+\frac{z_0^3}{6}+\frac{z_0^5}{120}+\frac{z_0^7}{5040}\right)
>
\frac{100013}{100000}.
\tag{12}
\]

Therefore

\[
\boxed{\mathcal A(S_0,q_0)>1.00013>1.}
\tag{13}
\]

By monotonicity, every `q>q_0` and `S>=S_0` has `mathcal A(S,q)>1`.

For completeness, this strict hyperbolic inequality also excludes an exact zero rather than merely a negative value. Since `q>0`, the heights are unequal. When `mathcal A>1`, the amplitude mismatch in `ANF-042` is strictly larger than one for every `|alpha|>alpha_d`. Its exact phase minimum then has `R>1` and hence contains the strictly positive term `R^2-R`. In the residual separation range (5), `alpha_d=1/(3|d|)<1`, while the Montgomery--Taylor spectrum `J_MT=g*g` from `ANF-059` is strictly positive on `(-1,1)` because `g` is strictly positive on `[-1/2,1/2]`. Thus an open interval `alpha_d<|alpha|<1` contributes strictly positively. The integrated defect cannot vanish.

Consequently every zero or negative defect satisfies

\[
\boxed{S<\frac{2971}{2000}=1.4855,}
\tag{14}
\]

which is the third inequality in (1).

## 3. The residual vertical domain is now explicit

Combining (5) and (14),

\[
y_1+y_2
=S|d|
<\frac{2971}{2000}\frac{101}{100}
=\frac{300071}{200000}
=1.500355.
\tag{15}
\]

Hence the mean height obeys

\[
\boxed{
y:=\frac{y_1+y_2}{2}<0.7501775.}
\tag{16}
\]

The current five-point base-zero domain can therefore be parameterized by

\[
0<y<0.7501775,
\qquad
0.1409<q<1,
\qquad
0.545<|d|<1.01,
\tag{17}
\]

with

\[
y_1=y(1+q),
\qquad
y_2=y(1-q).
\tag{18}
\]

This is not yet a compact closed box because the real-axis boundary `y=0` and the one-pair boundary `q=1` remain limiting faces. Those faces are already analytically controlled by `ANF-039`--`ANF-041`; they must be retained explicitly in any exhaustive interval certificate rather than replaced by sampled lower cutoffs. The new point is that no unspecified large-height constant remains: the only noncompact variable still requiring its own treatment is the common horizontal translation, which `ANF-045` scalarizes to the one-dimensional coherence coefficient `kappa_*`.

The bound is also intentionally conservative. Solving the exact equation `mathcal A(S,0.1409)=1` numerically places the true corner near `S=1.48539`, but that decimal is not evidence and is not used. The rational value `1.4855` is chosen because (12) certifies it with a visible margin using only positive Taylor terms.

## 4. Prior art, stress tests and next certificate

The derivation uses no new external theorem. The Montgomery--Taylor profile and its support are already anchored in `SOURCES.md`; the new content is the exact intersection of the canonical Mathia gates `ANF-049`, `ANF-057`, and `ANF-059`, together with the rational hyperbolic certificate (12). A targeted check of current Montgomery--Taylor/pair-correlation and recent finite-compression work did not identify an external result stating this two-pair complex-zero height box. No publication-level novelty claim is made, and no new source is load-bearing, so `SOURCES.md` is unchanged.

The decisive stress tests are monotonicity and strictness. Replacing `q>0.1409` by a non-strict lower value can only weaken the left side of (7), so the corner check (12) is the correct worst case. Replacing `|d|<1.01` by its endpoint enlarges the derived absolute height bound, so (15) is outward-safe. Finally, the strict-zero argument uses `alpha_d<1`; this follows from the already certified lower separation `|d|>0.545`, and `J_MT>0` on the resulting open high-frequency subinterval.

This finding does **not** decide Montgomery--Taylor five-point zero-freeness, does not control the common-translation Fourier supremum, does not certify a central-notch spectrum, and does not address larger conjugation-invariant multisets. Its durable contribution is to turn the live shape problem into an explicit bounded-height domain suitable for a validated interval/coherence certificate rather than an abstract compactness argument.