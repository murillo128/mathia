# ANF-017 — an edge-detuned finite real configuration kills the cubic scalar survivor

**Status:** `EXACT-DERIVED + RIGOROUS-FINITE-WITNESS + DECISIVE-NEGATIVE + STRUCTURAL-BOUNDARY`. The explicit cubic positive spectrum `J_*` from `ANF-016` survives every thermodynamic lattice-periodization test, but it does **not** survive the full finite real-configuration requirement of the universal affine scalar certificate. A 15-site configuration obtained by detuning only the two boundary gaps of an otherwise equally spaced block has normalized `F_*`-energy below the exact threshold `C(J_*)/C_MT`. Applying the affine inequality to that configuration and to the same sites with multiplicity two therefore forces the entire amplitude ray `tJ_*` back **below** the Montgomery--Taylor bound.

More precisely, let

\[
C_*:=C(J_*)=\frac{53}{40},
\qquad
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.327499296320588\ldots .
\]

There is an explicit 15-point real set `X_*` for which

\[
\boxed{
e_*(X_*):=\frac1{15}\sum_{x,y\in X_*}F_*(x-y)
=0.998079905262228\ldots
}
\]

and hence

\[
\boxed{
\frac{C_*}{e_*(X_*)}
=1.327549019887219\ldots
>C_{\rm MT}.
}
\]

Consequently no scaling `tJ_*` can give a universal-affine simple-critical-zero bound above

\[
\boxed{
2-\frac{C_*}{e_*(X_*)}
=0.672450980112780\ldots
<2-C_{\rm MT}
=0.672500703679411\ldots .
}
\]

The thermodynamic escape of `ANF-016` is therefore real but finite-volume: it disappears before one needs a vertically displaced or otherwise complex configuration.

## 1. Finite real configurations have their own scale-free ratio

Keep the residual universal affine setup of `ANF-013` and `ANF-016`. For a continuous even spectrum `J>=0` supported in `[-1,1]`, put

\[
F=\widehat J,
\qquad
C=C(J),
\]

and suppose one seeks, for every finite conjugation-invariant multiset `Z`, a certificate

\[
s(Z)\ge A|Z|-E_F(Z),
\qquad
E_F(Z)=\sum_{z,w\in Z}F(z-w).
\tag{1}
\]

Let `X={x_1,...,x_n}` be any finite set of **distinct real** points and define its normalized energy

\[
e_J(X):=\frac1n E_F(X)
=\frac1n\sum_{i,j=1}^nF(x_i-x_j).
\tag{2}
\]

Because `J>=0`, Fourier inversion gives

\[
e_J(X)
=\frac1n\int_{-1}^{1}J(\alpha)
\left|\sum_{j=1}^ne^{-2\pi i\alpha x_j}\right|^2d\alpha
\ge0.
\tag{3}
\]

Now scale the spectral shape by `t>0`. The simple configuration `X` has `s(X)=|X|=n`, so (1) gives

\[
A\le1+t e_J(X).
\tag{4}
\]

If every site of `X` is duplicated, no element is simple, the multiset has size `2n`, and its energy is `4tE_F(X)`. Thus

\[
A\le2t e_J(X).
\tag{5}
\]

Combining (4)--(5),

\[
A\le\psi\!\left(t e_J(X)\right),
\qquad
\psi(u)=\min(1+u,2u).
\tag{6}
\]

The BGSST cost of the scaled profile is `tC`, so this single finite support gives

\[
B_t:=A-tC
\le
\psi(te)-tC,
\qquad e=e_J(X).
\tag{7}
\]

Exactly as in the amplitude optimization of `ANF-013`, if `e>0` then

\[
\boxed{
\sup_{t>0}\bigl(\psi(te)-tC\bigr)
=
\max\left\{0,2-\frac Ce\right\}.
}
\tag{8}
\]

Thus a finite real configuration is not merely a fixed-normalization test. The scale-free quantity is again a **ratio**, now `C/e_J(X)`.

Define the full finite-real floor

\[
q_{\rm real}(J)
:=\inf_{\substack{X\subset\mathbb R\\0<|X|<\infty}}
e_J(X),
\tag{9}
\]

where `X` ranges over finite sets of distinct real points. Long arithmetic progressions are a subfamily, so the Fejer limit of `ANF-013` gives

\[
q_{\rm real}(J)\le p(J).
\tag{10}
\]

Whenever `q_real(J)>0`, a necessary condition for the shape `J` to beat Montgomery--Taylor through a universal affine certificate is therefore

\[
\boxed{
\frac{C(J)}{q_{\rm real}(J)}<C_{\rm MT}.
}
\tag{11}
\]

If `q_real(J)=0`, the shape is already useless for a positive universal-affine bound.

## 2. The cubic survivor and its exact spatial kernel

Use the cubic spectrum from `ANF-016`:

\[
J_*(x)
=1-\frac38|x|-\frac74|x|^2+\frac98|x|^3
\qquad(|x|\le1),
\tag{12}
\]

with `J_*(x)=0` outside `[-1,1]`. Its BGSST cost and thermodynamic floor are

\[
C_* = \frac{53}{40},
\qquad
p(J_*)=1.
\tag{13}
\]

For real `u\ne0`, its Fourier transform is

\[
F_*(u)=
\frac{
2\pi^2u^2(3-4\cos 2\pi u)
-26\pi u\sin 2\pi u
-27\cos 2\pi u+27
}{32\pi^4u^4},
\tag{14}
\]

with

\[
F_*(0)=\frac{49}{48}.
\tag{15}
\]

The thermodynamic periodization floor `p(J_*)=1` made the amplitude-optimized long-lattice cap equal to `2-53/40=0.675`, leaving apparent room above Montgomery--Taylor. Equation (11) asks whether a **finite** real support can lower the relevant energy floor enough to erase that room.

## 3. A two-scale 15-site witness

Take 15 ordered real sites with consecutive gaps

\[
\boxed{
\left(
\frac{21}{20},
\underbrace{\frac{41}{40},\ldots,\frac{41}{40}}_{12\text{ gaps}},
\frac{21}{20}
\right).
}
\tag{16}
\]

Equivalently, put

\[
a=\frac{21}{20},
\qquad
b=\frac{41}{40},
\]

and define

\[
X_*=
\{0\}
\cup
\{a+mb:0\le m\le12\}
\cup
\{2a+12b\}.
\tag{17}
\]

So the central 13 sites form an arithmetic progression of spacing `41/40`; only the two boundary gaps are enlarged, from `41/40` to `21/20`. This is the smallest structural change needed here: no irregular bulk, no vertical displacement, and no complex geometry.

Grouping pair distances in (2) gives the exact finite identity

\[
\boxed{
\begin{aligned}
e_*(X_*)
={}&F_*(0)
+\frac{2}{15}\Bigg[
\sum_{m=1}^{12}(13-m)F_*(mb)\\
&\qquad\qquad
+2\sum_{m=0}^{12}F_*(a+mb)
+F_*(2a+12b)
\Bigg].
\end{aligned}
}
\tag{18}
\]

Every argument of `F_*` in (18) is a rational with denominator `40`. Hence (14) reduces the entire certificate to finitely many values of sine and cosine at multiples of `pi/20` together with rational arithmetic and powers of `pi`.

## 4. Rigorous finite evaluation

Direct interval evaluation of the exact expression (18) gives

\[
\boxed{
0.99807990526222
<e_*(X_*)
<0.99807990526224.
}
\tag{19}
\]

This enclosure can be checked without assuming any floating-point identity: reduce the trigonometric arguments in (14) to `[0,pi/2]`, enclose `pi` rationally, and use alternating Taylor bounds for `sin` and `cos`. Because all phases are multiples of `pi/20`, the calculation is finite and elementary. In particular the much coarser rational inequality

\[
e_*(X_*)<0.9981
\tag{20}
\]

already suffices for the sign of the final comparison.

Indeed,

\[
\frac{C_*}{0.9981}
=1.327522292355475\ldots
>1.3275
>C_{\rm MT},
\tag{21}
\]

where the last inequality follows from the exact Montgomery--Taylor value

\[
C_{\rm MT}=1.327499296320588\ldots .
\]

Using the sharper enclosure (19),

\[
1.327549019887203
<\frac{C_*}{e_*(X_*)}
<1.327549019887231.
\tag{22}
\]

Substituting (22) into (8) proves for the **entire amplitude ray** `tJ_*` that

\[
\boxed{
B_t\le0.672450980112797\ldots
<0.672500703679411\ldots
=2-C_{\rm MT}.
}
\tag{23}
\]

Thus the cubic thermodynamic survivor is decisively eliminated by a finite real configuration.

## 5. Why fixed-amplitude finite lattices are not the right criterion

The decisive point is the reoptimization in (8). Once finite-volume energy drops below the thermodynamic normalization `p(J_*)=1`, testing only the normalized profile `t=1` can make a configuration look stronger than it really is: the scalar certificate is free to rescale the entire spectral shape until the simple and duplicated constraints meet again at `t e=1`.

Therefore a finite arithmetic progression kills a **shape** only when its normalized energy `e` satisfies

\[
\frac{C_*}{e}\ge C_{\rm MT},
\tag{24}
\]

not merely when its fixed-amplitude intercept happens to fall below `C_*+2-C_MT`. The exact ratio formulation (8) is the finite-volume analogue of the thermodynamic ratio `C/p` in `ANF-013` and is the correct quantity to carry forward.

The witness (16) crosses (24). Its advantage over the long-lattice tests is specifically a boundary degree of freedom: two edge gaps detune while the bulk remains periodic. This is information erased by the Fejer thermodynamic limit.

## 6. Falsification and scope boundary

The configuration `X_*` consists of distinct real points, so both `X_*` and its duplicated multiset are among the configurations quantified over by the universal inequality (1). Multiplicity scaling is exact, `J_*>=0` makes the energy representation (3) nonnegative, and the comparison uses no zeta-zero asymptotic beyond the already established BGSST cost `C_*`.

This finding does **not** prove a Montgomery--Taylor ceiling for every positive support-one spectrum. It eliminates only the explicit cubic shape `J_*` and all of its positive amplitude scalings. Other spatially signed kernels with `J>=0` may still satisfy `C(J)/q_real(J)<C_MT`.

It also does not constrain the configuration-level route of `ANF-006`, non-affine counting inequalities, matrix/inertia information used before scalar compression, or zeta-specific inequalities that do not quantify over arbitrary finite conjugation-invariant multisets.

## 7. Prior-art and next boundary

Positive-definite finite energies, Fejer kernels, Fourier representations such as (3), and the use of finite point configurations to test bandlimited kernels are classical. The Montgomery--Taylor extremal constant and its nonnegative-spatial support-one boundary remain anchored by Carneiro--Chandee--Littmann--Milinovich in `SOURCES.md`. A targeted search across finite Fourier-energy tests, positive-definite bandlimited extremal problems, pair-correlation simple-zero bounds, and arithmetic-progression/Fejer constraints did not locate the specific ratio reduction (8)--(11) or the explicit edge-detuned witness (16) in this universal affine simple-critical-zero setting. No publication-level novelty claim is made.

The scalar frontier is now sharper than the finite-lattice question left by `ANF-016`. The natural shape functional is

\[
\boxed{
R_{\rm real}(J):=\frac{C(J)}{q_{\rm real}(J)}.
}
\tag{25}
\]

A universal theorem `R_real(J)>=C_MT` for every continuous even `J>=0` supported in `[-1,1]` would close the entire residual universal-affine scalar branch **using real configurations alone**. Conversely, a new profile with `R_real(J)<C_MT` would justify the next stage: test arbitrary finite real configurations more deeply and only then move to vertically displaced conjugate configurations. `ANF-017` shows that thermodynamic survival is not enough; even a two-gap boundary relaxation can expose the missing finite-volume obstruction.
