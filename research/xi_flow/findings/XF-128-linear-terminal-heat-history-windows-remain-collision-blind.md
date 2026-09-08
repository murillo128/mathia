# XF-128 — linear terminal heat-history windows remain collision-blind

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `TERMINAL-WINDOW` + `FULL-HISTORY-NONIDENTIFIABILITY` + `COLLISION-MATCHED-CONTROL`. XF-127 shows that the complete terminal history `P_N(s)` does not determine collision geometry: a near-balanced two-shell family has a phase fiber along which `P_N(s)` is identical while the target crosses the collision discriminant. The natural next repair is to add nearby high harmonics and ask whether a short terminal window breaks that fiber.

It does not merely fail for a few extra coordinates. The same two-shell mechanism can hide the collision from a **linear number of consecutive terminal harmonic histories**. More precisely, choose coprime integers

\[
1\le a<b<2a
\tag{1}
\]

of opposite parity, let `g>=1`, and set

\[
N=(a+b)g,
\qquad
r=ag,
\qquad
d=bg=N-r.
\tag{2}
\]

Then there are two degree-`N` unit-circle targets, one with exactly `g` isolated double roots and one with all roots simple, such that under the exact XF-067 coefficient heat flow

\[
\boxed{
P_m^{\rm coll}(s)=P_m^{\rm simple}(s)
\qquad
\text{for every }s\ge0
\text{ and every }d<m\le N.
}
\tag{3}
\]

The matched terminal window contains exactly

\[
N-d=r
\tag{4}
\]

harmonic coordinates, hence a fraction

\[
\boxed{\frac rN=\frac{a}{a+b}}
\tag{5}
\]

of the entire first-`N` harmonic interface. The colliding target has collision-slot density

\[
\boxed{\frac{2g}{N}=\frac{2}{a+b}.}
\tag{6}
\]

Taking `b=a+1` makes the matched-window fraction

\[
\frac{a}{2a+1}\longrightarrow\frac12.
\tag{7}
\]

Consequently, for every fixed `theta<1/2` there are arbitrarily large degrees and a fixed positive collision density (depending on `theta`) for which **all complete harmonic histories in a terminal window of at least `theta N` consecutive coordinates are exactly identical** between a colliding target and an all-simple target.

The result also identifies the first place where this particular phase fiber is exposed. The immediately preceding active shell `m=d` changes sign between the two controls, so adding `P_d(s)` breaks the matched pair exactly. Thus the theorem does not claim a universal half-degree lower bound for every possible control family; it gives an exact linear blind window, approaching half the spectrum, together with its sharp boundary inside the XF-127 two-shell construction.

## 1. Use the XF-127 collision phase and its simultaneous sign flip

For unit phases `U,V`, consider

\[
E_{U,V}(z,0)
=(1+Uz^r)(1+Vz^d).
\tag{8}
\]

As in XF-127, the two cyclic root sets intersect if and only if

\[
V^a=(-1)^{a-b}U^b.
\tag{9}
\]

Because `a` and `b` have opposite parity, `a-b` is odd. Fix any compatible pair `(U,V)` satisfying `(9)`; for example one may impose `UV=1` and choose

\[
U^{a+b}=-1,
\qquad
V=U^{-1}.
\tag{10}
\]

The target

\[
E_{\rm c}(z,0):=(1+Uz^r)(1+Vz^d)
\tag{11}
\]

then has exactly `g` common roots between its two factors, hence exactly `g` isolated double roots and all other roots simple.

Now flip both phases:

\[
U_{\rm s}:=-U,
\qquad
V_{\rm s}:=-V,
\tag{12}
\]

and define

\[
E_{\rm s}(z,0):=(1-Uz^r)(1-Vz^d).
\tag{13}
\]

The terminal product is unchanged,

\[
U_{\rm s}V_{\rm s}=UV=:W.
\tag{14}
\]

But collision compatibility is destroyed. Indeed, if `(9)` holds then

\[
V_{\rm s}^a=(-1)^aV^a,
\qquad
(-1)^{a-b}U_{\rm s}^b
=(-1)^{a-b+b}U^b,
\tag{15}
\]

and equality between these two expressions would require `(-1)^a=(-1)^b`, contrary to the opposite parity assumption. Thus the two cyclic factors in `(13)` are disjoint and every root of `E_s` is simple.

This is the same collision/simple phase crossing as XF-127, but the simultaneous sign flip has one extra feature that was not used there: it preserves every **even** monomial in the proper shell amplitudes.

## 2. Below degree `N`, the two-shell logarithm has only three active harmonics

Under XF-067's exact diagonal coefficient heat flow,

\[
E_k(s)=E_k(0)e^{-\delta_k s},
\qquad
\delta_k=\frac{4\pi^2}{L^2}k(N-k).
\tag{16}
\]

Since `d=N-r`, one has `delta_r=delta_d`; write

\[
q(s):=e^{-\delta_r s}.
\tag{17}
\]

The two evolved coefficient polynomials are therefore

\[
E_{\rm c}(z,s)
=1+Uqz^r+Vqz^d+Wz^N,
\tag{18}
\]

and

\[
E_{\rm s}(z,s)
=1-Uqz^r-Vqz^d+Wz^N.
\tag{19}
\]

Newton's logarithmic identity is

\[
\log E(z,s)
=
\sum_{m\ge1}(-1)^{m-1}\frac{P_m(s)}m z^m.
\tag{20}
\]

For every proper degree `m<N`, the terminal monomial `Wz^N` cannot contribute to `[z^m] log E`. Hence only nonnegative combinations of `r` and `d` matter. The near-balanced inequalities

\[
\frac N3<r<\frac N2<d<\frac{2N}{3}
\tag{21}
\]

make the proper additive support completely explicit. If

\[
m=kr+\ell d<N,
\qquad k,\ell\in\mathbf Z_{\ge0},
\qquad k+\ell\ge1,
\tag{22}
\]

then `ell>=1` forces `ell=1,k=0`, giving `m=d`; while `ell=0` allows only `k=1,2`, giving `m=r` or `m=2r`. Thus

\[
\boxed{
\operatorname{supp}\{P_m(s):1\le m<N\}
\subseteq\{r,d,2r\}
}
\tag{23}
\]

for both controls, for every heat time `s>=0` at coefficient level.

Moreover `d<2r<N` because `b<2a`. The only potentially nonzero proper harmonic strictly above `d` is therefore `m=2r`. From `(20)`,

\[
[z^{2r}]\log E_{\rm c}
=[z^{2r}]\log E_{\rm s}
=-\frac12U^2q^2,
\tag{24}
\]

since the simultaneous sign flip leaves `U^2` invariant. Hence

\[
P_{2r}^{\rm coll}(s)=P_{2r}^{\rm simple}(s)
\qquad(s\ge0),
\tag{25}
\]

while every other proper mode with `d<m<N` vanishes identically in both trajectories.

This already proves equality of **all proper histories in the terminal interval `(d,N)`**, not just equality at one slice or to finite time-jet order.

## 3. The terminal harmonic is also unchanged

At degree `N`, the terminal coefficient enters. Because `r,d>N/3`, no product of three proper active monomials can sum to `N`; because `r+d=N`, the only proper contribution is the quadratic cross term. Exactly as in XF-127,

\[
[z^N]\log E(z,s)
=W-Wq(s)^2,
\tag{26}
\]

and therefore

\[
\boxed{
P_N(s)
=(-1)^{N-1}N W\left(1-e^{-2\delta_r s}\right).
}
\tag{27}
\]

The simultaneous sign flip preserves `W=UV`, so the two terminal histories agree exactly. Combining `(25)--(27)` with the zero histories between the active degrees proves `(3)`.

The mechanism is worth separating from XF-125. There the observer had only `o(N)` proper histories and the cyclic generator was chosen to make the complete additive cascade avoid the queried set. Here the queried set is a **fixed contiguous block of Theta(N) harmonics and includes the terminal mode itself**. Avoidance alone cannot work because `N` is a forced resonance. Instead, terminal resonance sees only the sign-even product `UV`, while the only other active mode inside the window sees only the sign-even square `U^2`. The collision condition is sign-odd because `a` and `b` have opposite parity. The observed terminal block therefore lies entirely in the even quotient of a phase fiber that crosses the discriminant.

## 4. The blind window can approach half of all harmonic coordinates

The number of matched coordinates in `(3)` is exactly

\[
\#\{m:d<m\le N\}=N-d=r,
\tag{28}
\]

so its relative width is `a/(a+b)`. The simplest quantitative family is

\[
b=a+1,
\qquad a\ge2.
\tag{29}
\]

These integers are automatically coprime and of opposite parity, and `b<2a`. Along degrees

\[
N=(2a+1)g,
\tag{30}
\]

we obtain a matched terminal fraction

\[
\rho_{\rm win}
=\frac{a}{2a+1}
=\frac12-\frac{1}{4a+2},
\tag{31}
\]

and collision-slot density

\[
\rho_{\rm coll}
=\frac{2}{2a+1}>0.
\tag{32}
\]

For each fixed `a`, the collision density remains macroscopic as `g to infinity`. Letting the fixed parameter `a` grow across families makes the blind window approach one half of the entire harmonic spectrum. Equivalently, for every `theta<1/2`, choose `a` once so that `a/(2a+1)>theta`; then arbitrarily large multiples `g` give a positive-density colliding/simple pair whose top `theta N` complete harmonic histories are all identical.

The `2:3` instance from XF-127 is already striking. With

\[
a=2,
\qquad b=3,
\qquad N=5g,
\qquad r=2g,
\qquad d=3g,
\tag{33}
\]

the colliding and simple controls agree on every history

\[
P_m(s),
\qquad
3g<m\le5g,
\qquad
s\ge0.
\tag{34}
\]

Thus **40% of all harmonic coordinates, consecutively at the degree edge and including `P_N`, are jointly blind**, while 40% of the colliding target's root slots belong to double collisions.

This is a stronger information-theoretic obstruction than either XF-125 or XF-127 separately: the former allowed only a sublinear number of arbitrary proper histories, and the latter only the single terminal history.

## 5. The first omitted active shell breaks this exact phase fiber

The construction also gives a clean internal boundary. At `m=d`, no lower combination reaches degree `d` because `r<d<2r` and `gcd(a,b)=1`. Hence

\[
[z^d]\log E_{\rm c}=Vq,
\qquad
[z^d]\log E_{\rm s}=-Vq,
\tag{35}
\]

so

\[
\boxed{
P_d^{\rm coll}(s)=-P_d^{\rm simple}(s)\ne0
}
\tag{36}
\]

up to the common Newton parity normalization. Therefore extending the contiguous observed window by precisely the shell `d` separates this matched pair.

Combined with the terminal history, `P_d` is in fact enough to recover the two phase parameters within the two-shell model: `(27)` recovers `W=UV`, while `(35)` recovers `V`, hence `U=W/V`. The collision compatibility `(9)` is then decidable. So the theorem should not be read as saying that every terminal window shorter than half the spectrum is universally insufficient, or that every window of half the spectrum is sufficient. What is exact is the family-specific statement:

\[
\boxed{
\{P_m(\cdot):d<m\le N\}
\text{ is nonidentifying, while adding }P_d(\cdot)
\text{ resolves this phase fiber.}
}
\tag{37}
\]

That sharp boundary is useful for the next observability test: a successful degree-scale Xi interface must hit a genuinely **phase-bearing active shell**, not merely accumulate many terminal coordinates whose Newton expansions collapse to even invariants.

## 6. Transition status remains different

Choose `g` even, as in XF-127's periodic matched-control normalization. The `g` common roots of `E_c(z,0)` are isolated doubles. The collision-safe local discriminant law used in XF-125--XF-127 makes those pairs leave the real periodic divisor immediately under backward heat, while forward real-root preservation keeps the divisor real for nonnegative heat. Hence

\[
\Lambda_{\rm per}^{\rm coll}=0.
\tag{38}
\]

Every root of `E_s(z,0)` is simple. Openness of simple real-rootedness under the finite coefficient flow gives a nonzero backward interval on which they remain real; together with forward preservation,

\[
\Lambda_{\rm per}^{\rm simple}<0.
\tag{39}
\]

Thus the entire matched terminal block in `(3)` cannot determine even the transition status of the target slice.

As in XF-127, this is a finite periodic matched-control theorem. It does **not** assert that the actual Xi degree-scale high-harmonic histories equal these controls, nor that Xi itself admits both realizations. Its role is to rule out a universal inference principle based solely on observing a large terminal block of scalar harmonic histories.

## 7. Prior-art and novelty boundary

The load-bearing ingredients are internal and elementary: XF-067's diagonal periodic coefficient flow, Newton's logarithmic identity, and the exact two-binomial collision condition already derived in XF-127. A directed literature audit covered unit-circle/self-inversive polynomial root criteria, Newton sums for sparse polynomials, and modern periodic backward-heat work. The latter remains represented in `SOURCES.md` by Kabluchko's unitary-Hermite paper and the Hall--Ho heat-flow reference. I did not find an external result matching the specific statement here: exact equality of a **linear consecutive terminal window of complete harmonic heat histories** across a positive-density colliding/simple unit-circle pair, with an explicit first-shell observability boundary.

No new external theorem is used in the proof, so `SOURCES.md` requires no update.

## Consequence for `xi_flow`

XF-127 asked for the smallest additional history coordinate that breaks its `U,V` phase fiber. XF-128 answers that question more sharply than expected. There need not be any useful information in the next few terminal harmonics—or even in a linear number of them. In the `2:3` family, the top 40% of the complete harmonic-history vector is exactly nonidentifying. Across the `a:(a+1)` family, the blind fraction approaches one half.

The next positive gate is therefore not "add a terminal window." It is to identify which **active Vieta shell phases** a degree-scale Xi observable actually exposes. In this model the first useful extra coordinate is `P_d`, because it is phase-odd and, together with `P_N`, resolves the collision fiber. A source-specific advance should target an observable with that kind of phase sensitivity or a joint full-degree transform that provably cannot quotient out the collision discriminant.