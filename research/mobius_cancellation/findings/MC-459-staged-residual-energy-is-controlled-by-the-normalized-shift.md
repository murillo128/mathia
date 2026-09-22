# MC-459 — Staged residual energy is controlled by the normalized shift, not by the quotient slopes

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The first quantitative test left open by `MC-458` can be resolved at the level of the **positive residual-weight energy**. In the staged factorization, progression concentration of the two residual divisor-sum amplitudes does not by itself recreate a polynomial source-frame tariff.

Write

\[
r=g r_1,
\qquad
r'=g r_2,
\qquad
(r_1,r_2)=1,
\qquad
h=g h_0\ne0,
\tag{1}
\]

and let

\[
R=[r,r']=g r_1r_2.
\tag{2}
\]

For the unique contributing CRT class `n=a+Rk` from `MC-458`, set

\[
y_1(k)=\frac{n+h}{r}=A_1+r_2k,
\qquad
y_2(k)=\frac n{r'}=A_2+r_1k.
\tag{3}
\]

Then these two affine quotient forms satisfy the exact relation

\[
\boxed{r_1y_1(k)-r_2y_2(k)=h_0.}
\tag{4}
\]

Consequently

\[
(r_2,A_1)=(r_2,h_0),
\qquad
(r_1,A_2)=(r_1,h_0).
\tag{5}
\]

Thus a divisor modulus can concentrate on one quotient progression only through the normalized shift `h_0=h/g`; the possibly large slopes `r_1,r_2` do not create an independent singularity.

More strongly, let

\[
B_\beta(y)=\sum_{\substack{s\mid y\\s\le S}}\beta_s,
\qquad |\beta_s|\le1,
\tag{6}
\]

and let `I` be an interval of `K` consecutive `k` values. For the one-sided second moment, if `L=[s,t]` and `d=(L,r_2)`, then

\[
\#\{k\in I:L\mid A_1+r_2k\}
=
\begin{cases}
K\,d/L+O(1),& d\mid h_0,\\
0,&d\nmid h_0.
\end{cases}
\tag{7}
\]

The analogous formula holds for `y_2`. Hence the bulk density contribution is controlled by `(h_0,r_i)`, not by `r_i` itself.

The coupled positive diagonal is even cleaner. Put

\[
L_1=[s,t],
\qquad
L_2=[u,v],
\qquad
G=(r_1L_1,r_2L_2).
\tag{8}
\]

The conditions `L_1|y_1(k)` and `L_2|y_2(k)` are compatible exactly when

\[
G\mid h_0.
\tag{9}
\]

When compatible, their density inside the base CRT progression is exactly

\[
\boxed{
\frac{R}{[rL_1,r'L_2]}
=
\frac{G}{L_1L_2}.
}
\tag{10}
\]

Therefore compatibility forces the bulk density bound

\[
\frac{G}{L_1L_2}
\le
\frac{|h_0|}{L_1L_2}.
\tag{11}
\]

If

\[
C_2(S):=\sum_{s,t\le S}\frac1{[s,t]},
\tag{12}
\]

then

\[
C_2(S)\ll (1+\log S)^3,
\tag{13}
\]

and direct divisor expansion gives the bulk estimate

\[
\boxed{
\sum_{k\in I}|B_\beta(y_1(k))|^2|B_\beta(y_2(k))|^2
\ \le\ 
K|h_0|\,C_2(S)^2+O(S^4),
}
\tag{14}
\]

so the main congruence-density term is

\[
\ll K|h_0|(1+\log S)^6.
\tag{15}
\]

The raw `O(S^4)` endpoint in `(14)` is only an artifact of summing an `O(1)` counting error independently over every divisor quadruple; it is not a genuine short-progression polynomial obstruction. Indeed, if `y_1(k),y_2(k)\le X`, the pointwise divisor bound gives, for every fixed `\varepsilon>0`,

\[
|B_\beta(y_i(k))|\le \tau(y_i(k))\ll_\varepsilon X^{\varepsilon/4},
\tag{16}
\]

after rescaling `\varepsilon`, and therefore uniformly for every interval `I`,

\[
\boxed{
\sum_{k\in I}|B_\beta(y_1(k))|^2|B_\beta(y_2(k))|^2
\ll_\varepsilon K X^\varepsilon.
}
\tag{17}
\]

This closes one of the two failure modes posed after `MC-458`: **the true positive residual-weight diagonal is not forced to be polynomially larger merely because the affine quotient progressions concentrate divisibility.** The remaining difficulty is not norm inflation. It is extracting a strict conductor-power gain from the character-weighted staged kernel while the `B_\beta` factors are still coupled to the source variable and before absolute majorization, residual-divisor expansion, or outer-factor summation restores the product-level tariff.

No improved estimate for the weighted translated-character sum, no improvement to the `MC-415`/`MC-448` final source budget, no bound for `M(x)`, and no RH consequence follows.

## 1. The two quotient progressions have shift determinant `h_0`

From `(3)`,

\[
r_1y_1(k)-r_2y_2(k)
=
\frac{n+h}{g}-\frac n g
=h_0,
\tag{18}
\]

which proves `(4)`. Reducing `(4)` modulo `r_2` gives

\[
r_1A_1\equiv h_0\pmod{r_2}.
\tag{19}
\]

Since `(r_1,r_2)=1`, multiplication by `r_1` is invertible modulo every divisor of `r_2`, so

\[
(A_1,r_2)=(h_0,r_2).
\tag{20}
\]

The second identity in `(5)` is identical after reducing `(4)` modulo `r_1`.

There is a useful invariant formulation. Define the linear forms

\[
Q_1(k)=A_1+r_2k,
\qquad
Q_2(k)=A_2+r_1k.
\tag{21}
\]

Their determinant is

\[
r_2A_2-r_1A_1=-h_0,
\tag{22}
\]

and the discriminant of their product is therefore

\[
\operatorname{Disc}(Q_1Q_2)=h_0^2.
\tag{23}
\]

So the local singularity parameter of the paired quotient forms is the normalized shift, not the magnitude of either slope. This is exactly the structural feature one expects from the classical Nair--Tenenbaum/Henriot theory of arithmetic functions on polynomial values, where uniformity is organized by the discriminant. Equation `(23)` is derived here directly from the `MC-458` source geometry; the general discriminant-uniform theory is prior art, not a new theorem.

## 2. Exact one-progression divisor density

Fix `L>=1` and consider

\[
L\mid A_1+r_2k.
\tag{24}
\]

Let `d=(L,r_2)`. The congruence is soluble exactly when `d|A_1`. Because `d|r_2`, `(20)` shows

\[
d\mid A_1
\quad\Longleftrightarrow\quad
d\mid h_0.
\tag{25}
\]

When soluble, division by `d` leaves one residue class modulo `L/d`; therefore on `K` consecutive integers,

\[
\#\{k\in I:L\mid A_1+r_2k\}
=K\frac dL+O(1).
\tag{26}
\]

This proves `(7)`. Expanding one square,

\[
\sum_{k\in I}|B_\beta(y_1(k))|^2
=
\sum_{s,t\le S}\beta_s\overline{\beta_t}
\#\{k\in I:[s,t]\mid y_1(k)\},
\tag{27}
\]

so its bulk term is at most

\[
K(r_2,h_0) C_2(S).
\tag{28}
\]

The same argument gives `K(r_1,h_0)C_2(S)` on the second progression. This is already enough to rule out a slope-sized bulk concentration factor.

## 3. The coupled diagonal has an exact compatibility formula

For the coupled energy, expand both squares. A divisor quadruple `(s,t,u,v)` imposes

\[
L_1\mid y_1(k),
\qquad
L_2\mid y_2(k).
\tag{29}
\]

Returning to the original source integer `n=a+Rk`, these conditions are equivalent to

\[
rL_1\mid n+h,
\qquad
r'L_2\mid n.
\tag{30}
\]

Two residue classes in `(30)` are compatible exactly when

\[
(rL_1,r'L_2)\mid h.
\tag{31}
\]

Using `(1)`,

\[
(rL_1,r'L_2)=g(r_1L_1,r_2L_2)=gG,
\tag{32}
\]

so `(31)` is equivalent to `G|h_0`, proving `(9)`.

If compatible, the simultaneous congruence has period `[rL_1,r'L_2]` in `n`. Since the base class has period `R`, the corresponding period in `k` is

\[
\frac{[rL_1,r'L_2]}{R}.
\tag{33}
\]

Thus the exact relative density is

\[
\frac{R}{[rL_1,r'L_2]}.
\tag{34}
\]

Using `[A,B]=AB/(A,B)`, `(1)`, `(2)`, and `(32)`,

\[
\frac{R}{[rL_1,r'L_2]}
=
\frac{g r_1r_2\cdot gG}
     {g^2r_1r_2L_1L_2}
=
\frac{G}{L_1L_2},
\tag{35}
\]

which proves `(10)`. Since every contributing quadruple has `G|h_0`, `(11)` follows.

## 4. Bulk energy is polylogarithmic; the all-range diagonal is subpower

The elementary lcm sum obeys

\[
C_2(S)
=\sum_{s,t\le S}\frac{(s,t)}{st}.
\tag{36}
\]

Writing `s=da`, `t=db`, with `(a,b)=1`, and discarding the coprimality restriction for an upper bound gives

\[
C_2(S)
\le
\sum_{d\le S}\frac1d
\left(\sum_{a\le S/d}\frac1a\right)^2
\ll (1+\log S)^3,
\tag{37}
\]

proving `(13)`.

For each compatible quadruple, `(35)` gives

\[
\#\{k\in I:L_1\mid y_1(k),\ L_2\mid y_2(k)\}
=K\frac{G}{L_1L_2}+O(1).
\tag{38}
\]

Taking absolute values of the coefficient products and using `|\beta|<=1` gives `(14)` and `(15)`.

The endpoint term in `(14)` should not be interpreted as a real `S^4` diagonal. Without expanding at all,

\[
|B_\beta(y)|
\le
\sum_{s\mid y}1
=\tau(y).
\tag{39}
\]

The classical divisor estimate `\tau(m)\ll_\eta m^\eta` for every fixed `\eta>0` then proves `(17)` after choosing `\eta` small enough. This bound deliberately forgets the staged factor structure, so it cannot itself create the desired conductor saving. Its role is narrower and decisive: it proves that **mere positive-energy size is not the obstruction**.

In particular, if a later Cauchy/dispersion step produces the diagonal

\[
\sum_{k\in I}
|\chi(k+u+\delta)\overline{\chi(k+u)}|^2
|B_\beta(y_1(k))|^2|B_\beta(y_2(k))|^2,
\tag{40}
\]

then `(17)` still applies because the primitive-character factor has modulus at most one. Any polynomial loss must therefore enter elsewhere: through the off-diagonal completion/dispersion, outer `(r,r')` multiplicity, exceptional source ranges, or an analytic step that destroys the coupling before extracting cancellation.

## 5. Prior-art audit

Kevin Henriot's *Nair--Tenenbaum bounds uniform with respect to the discriminant*, Mathematical Proceedings of the Cambridge Philosophical Society 152 (2012), no. 3, 405--424, DOI `10.1017/S0305004111000752`, gives general short-sum bounds for submultiplicative arithmetic functions evaluated on polynomial values with explicit, optimal dependence on the polynomial discriminant. Henriot explicitly discusses shifted-convolution situations such as a product `X(X+ell)`, whose discriminant is `ell^2`. A 2014 erratum, DOI `10.1017/S0305004114000280`, corrects several details while stating that the claimed results are recovered with small modifications.

This is close prior art for the interpretation of `(23)`: two affine forms should be organized by their determinant/discriminant, and a shift-like parameter rather than the raw coefficient size controls the singular arithmetic interaction. It does **not** supply `(7)`--`(10)` as a new theorem here; those formulas are elementary CRT consequences specialized to the staged Mathia kernel. Conversely, this finding does not invoke Henriot as a black box for all source intervals: Nair--Tenenbaum-type theorems have interval-size and coefficient hypotheses that must be checked before transfer. The all-range statement `(17)` uses only the pointwise divisor bound.

The lcm-density manipulations themselves are classical. The Mathia-specific delta is the exact identification of the staged `MC-458` quotient pair with determinant `h/g`, and the consequence for the live branch: progression concentration cannot be dismissed heuristically, but after exact accounting it does not force a conductor-power positive diagonal.

## 6. Boundaries and falsification audit

1. **No oscillatory saving is proved.** Bounds `(14)`--`(17)` are positive-energy estimates. They say nothing about how much cancellation the translated primitive-character phase produces in the weighted sum.

2. **Absolute majorization is not the desired mechanism.** Equation `(17)` is intentionally too coarse to preserve factor-specific cancellation. Using it too early can still return the proof to the product-level occupancy regime classified by `MC-454`--`MC-455`.

3. **The normalized shift may vary.** The factor `|h_0|=|h|/g` in the explicit bulk estimate can itself be large. The stronger subpower envelope `(17)` avoids turning that factor into a mandatory loss, but does so by forgetting the arithmetic structure. A useful dispersion argument must keep track of the actual shift range and outer-factor averaging.

4. **Henriot is a boundary, not a transfer certificate.** His discriminant-uniform theorem does not automatically cover every incomplete interval, coefficient range, or weighted character phase appearing here. Any future use must verify its hypotheses and the 2014 corrections.

5. **No source-frame occupancy gain has yet been propagated.** The result removes one candidate obstruction but does not alter the existing `MC-415`/`MC-448` conductor budget by itself.

A decisive next test is therefore sharper than the one after `MC-458`: keep `(r,r')` outside and the two `B_\beta` amplitudes inside through the first genuine off-diagonal dispersion/completion step, then determine whether the nonzero frequency terms can gain a conductor power **without** expanding `B_\beta` back to `(s,t,u,v)` before cancellation. If the only available off-diagonal estimate requires that expansion or separate absolute majorants, the product quotient returns even though the diagonal itself is cheap.

## 7. Consequence for the research line

`MC-458` established that a legal pre-positive factor-specific carrier exists. This finding rules out the simplest quantitative reason it might fail: its residual divisor weights do not have a polynomially inflated progression-sensitive diagonal. The staged branch therefore remains live, but its burden has moved.

The live question is now specifically **off-diagonal and interference-sensitive**. A successful factorable argument must use the residual divisor-sum amplitudes while they are still coupled to the translated-character phase or to the outer factor family. A failure at that stage would be a substantially stronger no-go than the earlier observation that unrestricted `L^2` is polylogarithmic.

This is a narrowing result, not progress toward RH by itself.