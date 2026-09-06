# XF-073 — Gaussian-Appell periodization is relatively exact on the Xi high line

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC-LOCALIZATION` + `RELATIVE-PERIODIZATION` + `CLASSICAL-APPELL/THETA-INPUT`. XF-072 rules out suppressing a generic selected-zero seam merely by enlarging the periodic aspect ratio: the seam exposure and the local center frame both lose the same `1/R` factor. The accepted Gaussian-reference clue changes the object being periodized. Instead of periodically continuing a zero block, periodize exact backward-heat solutions after a Gaussian/Appell transform and divide by the periodized Gaussian reference.

For the actual Xi heat flow, the first missing source estimate in that clue can be proved. Fix `t_*>0`. Put

\[
\ell=\log T,
\qquad
\sigma_T^2=\ell^{3/2},
\qquad
L_T=\ell^3,
\qquad
a_T=A\ell,
\tag{1}
\]

where `A` is chosen as in XF-054 for the compact heat interval `[0,2t_*]`. For `0\le t\le t_*`, set

\[
h(t)=1-\frac{2t}{\sigma_T^2},
\qquad
v(t)=\sigma_T^2h(t)=\sigma_T^2-2t,
\qquad
s(t)=\frac{t}{h(t)},
\tag{2}
\]

and translate the Xi solution,

\[
u_T(z,s):=H_s(T+z).
\tag{3}
\]

Define the Gaussian/Appell pair

\[
V_T(z,t)
:=h^{-1/2}\exp\!\left(-\frac{z^2}{2v}\right)
 u_T\!\left(\frac zh,s\right),
\qquad
W_T(z,t)
:=h^{-1/2}\exp\!\left(-\frac{z^2}{2v}\right),
\tag{4}
\]

and their exact `L_T`-periodizations

\[
V_{T,L}(z,t)=\sum_{m\in\mathbb Z}V_T(z+mL_T,t),
\qquad
W_{T,L}(z,t)=\sum_{m\in\mathbb Z}W_T(z+mL_T,t).
\tag{5}
\]

Then both sums converge normally with every fixed number of `z` derivatives on the domains used below, and both solve the same backward heat equation. On the moving interior contour

\[
\mathcal C_T(t)
:=\left\{
 z=x+i h(t)a_T:\ |x|\le\frac{L_T}{4}
\right\},
\tag{6}
\]

the periodization is **relative-source exact**. For every fixed integer `J\ge0` there are constants `c_J>0` and `T_J` such that, for `T\ge T_J`,

\[
\boxed{
\max_{0\le j\le J}
\sup_{0\le t\le t_*}
\sup_{z\in\mathcal C_T(t)}
\left|
\partial_z^j\left(
\frac{V_{T,L}(z,t)}{V_T(z,t)}-1
\right)
\right|
\le
\exp\!\bigl(-c_J(\log T)^{9/2}\bigr).
}
\tag{7}
\]

The same estimate holds for `W_{T,L}/W_T-1`. Consequently `W_{T,L}` is zero-free on `\mathcal C_T(t)` for large `T`, and the known-reference quotient

\[
R_{T,L}:=\frac{V_{T,L}}{W_{T,L}}
\tag{8}
\]

satisfies

\[
\boxed{
\max_{0\le j\le J}
\sup_{t,z}
\left|
\partial_z^j\left(
\frac{R_{T,L}(z,t)}
{H_{s(t)}(T+z/h(t))}-1
\right)
\right|
\le
\exp\!\bigl(-c_J(\log T)^{9/2}\bigr),
}
\tag{9}
\]

where the supremum is over `0\le t\le t_*` and `z\in\mathcal C_T(t)`. Thus the Gaussian carrier is not being compared in absolute size: it cancels in the quotient, and the actual Xi solution is recovered with a super-polynomial **relative** error on the interior high line.

This closes the source-normalized `V_L/V-1` gate in the accepted Gaussian-reference clue. It does **not** yet prove stability of the forced quotient in the XF-070/XF-071 destination-weighted norm, nor that a hypothetical `Lambda>0` transition carries nonvanishing mass in that quotient. Those are now the live obligations.

## 1. The scaled Gaussian transform preserves backward heat exactly

The translated Xi field obeys

\[
(u_T)_s=-(u_T)_{zz}.
\tag{10}
\]

The transform (4) is the caloric Appell symmetry in a scaling convenient for this problem. It is also easy to verify directly. Since

\[
h'=-\frac2{\sigma_T^2},
\qquad
s'=h^{-2},
\qquad
\partial_t(z/h)=\frac{2z}{\sigma_T^2h^2},
\tag{11}
\]

and

\[
\frac{(W_T)_z}{W_T}=-\frac z v,
\qquad
\frac{(W_T)_{zz}}{W_T}=\frac{z^2}{v^2}-\frac1v,
\qquad
\frac{(W_T)_t}{W_T}=\frac1v-\frac{z^2}{v^2},
\tag{12}
\]

the chain rule and `(u_T)_s=-(u_T)_{zz}` give

\[
(V_T)_t=-(V_T)_{zz},
\qquad
(W_T)_t=-(W_T)_{zz}.
\tag{13}
\]

Normal convergence of (5) therefore permits termwise differentiation and proves that `V_{T,L}` and `W_{T,L}` are exact periodic backward-heat solutions. Their quotient obeys the exact known-drift equation

\[
\boxed{
(R_{T,L})_t
=-(R_{T,L})_{zz}
-2\frac{(W_{T,L})_z}{W_{T,L}}(R_{T,L})_z
}
\tag{14}
\]

wherever `W_{T,L}` is nonzero. Nothing in this step labels Xi zeros or assumes they are real.

## 2. Every interior image pays a quadratic Gaussian cost

For `z=x+iha_T`, division by the central image gives the exact identity

\[
\frac{V_T(z+mL_T,t)}{V_T(z,t)}
=
\exp\!\left(
-\frac{m^2L_T^2+2mL_Tz}{2v}
\right)
\frac{
H_s\!\left(T+(z+mL_T)/h\right)
}{
H_s\!\left(T+z/h\right)
}.
\tag{15}
\]

Because `|x|\le L_T/4`,

\[
m^2L_T^2+2mL_Tx
\ge
\left(m^2-\frac{|m|}{2}\right)L_T^2
\ge\frac{m^2L_T^2}{2}
\qquad(m\ne0),
\tag{16}
\]

so the Gaussian factor alone satisfies

\[
\left|
\exp\!\left(
-\frac{m^2L_T^2+2mL_Tz}{2v}
\right)
\right|
\le
\exp\!\left(-\frac{m^2L_T^2}{4v}\right).
\tag{17}
\]

The point of using the moving Xi high line is that the second factor in (15) grows only exponentially in the horizontal displacement with rate `O(log T)`, far slower than (17).

Indeed, for all sufficiently large `T`, `h\ge1/2` and `s=t/h\le2t_*`. If

\[
|m|L_T\le\frac T8,
\tag{18}
\]

then the central point and the shifted point in (15) both have real part in `[T/2,3T/2]`. XF-054, applied on the line `Im z=a_T`, gives uniformly there

\[
\frac{H_s'(X+ia_T)}{H_s(X+ia_T)}=O_{t_*}(\log T).
\tag{19}
\]

The line is zero-free by the unconditional de Bruijn strip theorem, so integrating (19) horizontally yields

\[
\left|
\frac{H_s(X+\delta+ia_T)}{H_s(X+ia_T)}
\right|
\le
\exp\!\bigl(C|\delta|\log T\bigr).
\tag{20}
\]

The fixed derivative bounds in XF-054, or equivalently Cauchy differentiation inside the same zero-free high-line region, add only fixed powers of `log T` and `|\delta|`. Substituting `|\delta|=|m|L_T/h` into (17)--(20) gives, for every fixed derivative order,

\[
\left|
\partial_z^j
\frac{V_T(z+mL_T,t)}{V_T(z,t)}
\right|
\le
P_j(T,m)
\exp\!\left(
-\frac{m^2L_T^2}{4v}
+C|m|L_T\log T
\right),
\tag{21}
\]

where `P_j` is only polynomial in the displayed polylogarithmic scales.

Now

\[
\frac{L_T}{v\log T}
\asymp
(\log T)^{1/2}\longrightarrow\infty,
\qquad
\frac{L_T^2}{v}
\asymp
(\log T)^{9/2}.
\tag{22}
\]

Hence the linear Xi growth term in (21) is eventually at most half of the quadratic Gaussian cost already for `|m|=1`. Summing all images satisfying (18) gives

\[
\sum_{0<|m|L_T\le T/8}
\left|
\partial_z^j
\frac{V_T(z+mL_T,t)}{V_T(z,t)}
\right|
\le
\exp\!\bigl(-c_j(\log T)^{9/2}\bigr).
\tag{23}
\]

This is the source-specific step. A generic entire heat solution could grow between neighboring images fast enough to defeat a chosen Gaussian; XF-054 rules that out for Xi on the moving high line.

## 3. Far images are even smaller

The remaining images lie outside the horizontal region where XF-054 gives the sharp logarithmic-derivative comparison, but they do not require a second delicate Xi asymptotic.

From the defining cosine-transform representation of `H_s`, the super-exponential decay of the de Bruijn kernel implies, for fixed `j` and `0\le s\le2t_*`,

\[
\sup_{X\in\mathbb R}
|H_s^{(j)}(X+ia)|
\le
\exp\!\bigl(C_j a\log(2+a)\bigr)
\qquad(a\ge2).
\tag{24}
\]

To see the scale, differentiating `j` times only inserts `u^j`; after taking absolute values, the integrand is bounded by `e^{su^2+a u}` times a kernel of the form `e^{O(u)-c e^{4u}}`. Its saddle is at `u=O(log(2+a))`, giving (24).

At the central denominator, XF-054's reflected Euler-product approximation together with Stirling gives the coarse but sufficient lower bound

\[
|H_s(T+x/h+ia_T)|\ge e^{-C T}
\qquad(|x|\le L_T/4).
\tag{25}
\]

Thus every fixed derivative of the Xi ratio in (15) is at worst `e^{CT+o(T)}` when the shifted image is arbitrary. But for the first far image, `|m|L_T>T/8`, equation (17) already gives

\[
\exp\!\left(-\frac{m^2L_T^2}{4v}\right)
\le
\exp\!\left(-\frac{T^2}{256v}\right)
=
\exp\!\left(-\Theta\!\left(\frac{T^2}{(\log T)^{3/2}}\right)\right).
\tag{26}
\]

This dominates the `e^{CT+o(T)}` denominator loss. The Gaussian tail in `m` then yields

\[
\sum_{|m|L_T>T/8}
\left|
\partial_z^j
\frac{V_T(z+mL_T,t)}{V_T(z,t)}
\right|
\le
\exp\!\left(-c_j\frac{T^2}{(\log T)^{3/2}}\right),
\tag{27}
\]

which is negligible compared with (23). Equations (23) and (27) prove (7), and simultaneously justify differentiated normal convergence of the periodization on the claimed domains.

## 4. The reference divides out its own artificial seam zeros

For the Gaussian reference, no Xi estimate is needed. Put

\[
\alpha_T(t):=\exp\!\left(-\frac{L_T^2}{4v(t)}\right).
\tag{28}
\]

Exactly as in (16)--(17), on `|Re z|\le L_T/4`,

\[
\left|\frac{W_{T,L}}{W_T}-1\right|
\le
\frac{2\alpha_T}{1-\alpha_T}.
\tag{29}
\]

Fixed `z` derivatives add only powers of `L_T/v`, so they are still `\exp(-\Theta((\log T)^{9/2}))`. In particular the right side of (29) is below one for large `T`, proving that `W_{T,L}` has no zero in the interior strip even though the full periodized Gaussian has known nonreal seam zeros outside it.

Since `V_T/W_T=u_T(z/h,s)`,

\[
\boxed{
\frac{R_{T,L}(z,t)}{H_s(T+z/h)}
=
\frac{V_{T,L}(z,t)/V_T(z,t)}
{W_{T,L}(z,t)/W_T(z,t)}.
}
\tag{30}
\]

Equations (7) and (29), followed by fixed-order quotient differentiation, prove (9). Thus the possibly tiny absolute Gaussian carrier never has to be lower-bounded: the estimate is intrinsically relative.

As a negative control, take `u_T\equiv1`. Then `V_T=W_T` and `R_{T,L}\equiv1` on every zero-free component of the reference. All auxiliary zeros created by Gaussian periodization cancel identically. This is exactly the behavior required from a reference construction; counting those zeros as Xi transition defects would be spurious.

## 5. Relation to XF-072 and the remaining gate

There is no contradiction with the XF-072 `1/R` obstruction. XF-072 periodizes a selected point block and extracts local zero information by a full-period center average. Here the periodized objects are exact heat solutions, the comparison is local and **relative** on an interior contour, and known Gaussian images are divided before any zero/state interpretation. The mechanism therefore lies outside the hypotheses of the XF-072 matched seam control.

What has been gained is narrower but concrete. The accepted Gaussian-reference clue asked first for a source-normalized estimate on `V_L/V-1` and its derivatives. Equations (7) and (9) supply such an estimate with super-polynomial room, in a parameter regime compatible with a fixed positive heat interval and without RH or a real-root assumption. The source side is no longer the immediate obstacle.

The next theorem must control (14) in the actual destination resource of XF-070--XF-071, including any finite-band truncation and normalization needed to compare with the guarded log-Vieta quotient. Only after such stability is available does it make sense to ask the separate transition question: whether `Lambda>0` forces order-one mass in that destination quotient. Nothing in XF-073 proves either statement, so it gives no new upper bound on `Lambda` and no RH consequence.

## 6. Prior art, falsification boundary, and audit tests

The caloric Appell transformation is classical. A modern peer-reviewed reference is Amalia Torre, **Appell Transformation and Canonical Transforms**, *SIGMA* 7 (2011), 072, DOI `10.3842/SIGMA.2011.072`, which explicitly treats the Appell symmetry for the one-dimensional heat equation and points back to Appell's 1892 work and Widder's heat-equation theory. Gaussian periodization and its theta-function structure are classical as well. XF-073 does not claim novelty for either ingredient.

A targeted search combining de Bruijn--Newman/Xi heat flow with Appell, Gaussian periodization, theta periodization, and reference quotients did not locate a source stating the specific moving-high-line relative estimate (7)--(9). The durable Mathia delta is therefore the reduction, not a claim that the surrounding heat symmetries are new: XF-054's Xi-specific high-line control is strong enough to make the Gaussian/Appell source interface exponentially accurate while preserving exact heat evolution.

The derivation has four direct failure tests. First, substituting any exact backward-heat solution into (4) must give zero residual in `partial_t+partial_z^2`; equations (11)--(13) show this symbolically. Second, the image ratio must contain the quadratic factor in (15); a sign error would destroy (17). Third, the central-image argument requires `L_T/(v\log T)\to\infty`; if `L_T` were only of order `v\log T`, the Xi horizontal growth could consume the Gaussian margin and this proof would not close. Fourth, the `u\equiv1` control must cancel every reference artifact in `R_{T,L}`; equation (30) does so exactly.

These controls also delimit the result. XF-073 is a source-interface theorem on a moving zero-free contour. It is not a theorem about all zeros of the periodic quotient, not a global real-rootedness statement, not a finite-degree Vieta representation, and not yet a bound in the destination-weighted state norm.