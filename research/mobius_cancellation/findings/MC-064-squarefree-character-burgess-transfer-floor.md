# MC-064 — Classical squarefree-character bounds put a direct quadratic transfer floor at exponent 11/16

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-CORRECTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let `X>=2`, let `q>X` be an odd prime, and let

\[
\chi(n)=\left(\frac{n}{q}\right)
\]

be the primitive quadratic character modulo `q`. Use the weighted Möbius-prime defect from `MC-060`--`MC-063`,

\[
A_X(\chi)
:=
\sum_{p\le X}\frac{|1+\chi(p)|}{p-1},
\tag{1}
\]

and the square-free-supported character comparator

\[
F_\chi(X)
:=
\sum_{n\le X}\mu(n)^2\chi(n).
\tag{2}
\]

Then the generator-to-prefix transfer already used in `MC-061` gives the exact approximation inequality

\[
\boxed{
|M(X)-F_\chi(X)|\le X A_X(\chi).
}
\tag{3}
\]

A targeted prior-art audit finds that the natural comparator sum `(2)` is itself a classical studied object. Munsch, *Character sums over squarefree and squarefull numbers*, Archiv der Mathematik 102 (2014), 555--563, DOI `10.1007/s00013-014-0658-9`, Lemma 2.3, proves for a nonprincipal character modulo `q`

\[
\left|\sum_{n\le x}\mu(n)^2\chi(n)\right|
\ll
x^{1/2}(\log x)q^{3/16+\varepsilon},
\tag{4}
\]

and notes that for prime `q` the factor `q^\varepsilon` in this version may be replaced by `(\log q)^{1/2}`. Therefore in the present prime-conductor setting,

\[
\boxed{
|M(X)|
\ll
X A_X(\chi)
+
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2}.
}
\tag{5}
\]

This is a genuine unconditional one-certificate transfer inequality. It sharpens the cruder termwise Pólya--Vinogradov certificate recorded in `MC-055` and makes the defect/conductor tradeoff explicit.

If, for fixed constants `1<kappa<2` and `beta>0`,

\[
X<q\le X^\kappa,
\qquad
A_X(\chi)\le X^{-\beta},
\tag{6}
\]

then `(5)` gives

\[
\boxed{
|M(X)|
\ll_{\kappa}
X^{1-\beta}
+
X^{1/2+3\kappa/16}(\log X)^{3/2}.
}
\tag{7}
\]

Thus this direct comparator architecture has two independent costs: the coefficient-transfer cost `X A_X` and the squarefree-character cancellation cost `X^(1/2)q^(3/16)`.

At power-exponent level, the classical Burgess/square-divisor certificate cannot reach an exponent below

\[
\boxed{\frac{11}{16}}.
\tag{8}
\]

Indeed `q>X`, so even the most favorable polynomial conductor scale `q=X^{1+o(1)}` leaves the comparator term in `(5)` at the `X^{11/16+o(1)}` level. More formally, to make the displayed comparator term at most `X^{1/2+epsilon}` would require

\[
q\le X^{16\varepsilon/3+o(1)},
\tag{9}
\]

which contradicts `q>X` whenever `epsilon<3/16`.

This is a **method-specific certification floor**, not a lower bound for the true character sum and not a lower bound for `M(X)`. A stronger theorem for squarefree character sums, a signed use of the square-divisor convolution, or a different comparator mechanism could in principle beat it. The finding says that the already-classical direct Burgess transfer does not close the RH-scale gap, even if the local defect were made arbitrarily small.

## 1. Weighted prime agreement controls coefficient disagreement on the whole prefix

Put

\[
g(n)=\lambda(n)\chi(n),
\]

where `lambda(n)=(-1)^{Omega(n)}`. Since `q>X`, every prime through `X` is coprime to `q`, and at such a prime

\[
|1-g(p)|=|1+\chi(p)|.
\tag{10}
\]

For every `n<=X`, complete multiplicativity and repeated use of

\[
|1-zw|\le |1-z|+|1-w|
\qquad(|z|=|w|=1)
\]

give

\[
|1-g(n)|
\le
\sum_p v_p(n)|1-g(p)|.
\tag{11}
\]

Summing over `n<=X`,

\[
\begin{aligned}
\sum_{n\le X}|1-g(n)|
&\le
\sum_{p\le X}|1-g(p)|
\sum_{j\ge1}\left\lfloor\frac{X}{p^j}\right\rfloor\\
&\le
X\sum_{p\le X}\frac{|1+\chi(p)|}{p-1}\\
&=XA_X(\chi).
\end{aligned}
\tag{12}
\]

Now compare Möbius with the square-free comparator coefficientwise. If `n` is not square-free, both `mu(n)` and `mu(n)^2 chi(n)` vanish. If `n` is square-free, then `mu(n)=lambda(n)` and hence

\[
|\mu(n)-\mu(n)^2\chi(n)|
=
|\lambda(n)-\chi(n)|
=
|1-\lambda(n)\chi(n)|.
\tag{13}
\]

Therefore

\[
\sum_{n\le X}
|\mu(n)-\mu(n)^2\chi(n)|
\le
XA_X(\chi),
\tag{14}
\]

and `(3)` follows by the triangle inequality.

The point is quantitative. The fixed defect budget `A_X(chi)<=c<1/2` used in `MC-060`--`MC-063` is strong enough to force character repulsion and multiscale rigidity, but `(3)` shows that it is still only a **linear** approximation budget for transferring an upper bound to `M(X)`. A direct power-saving transfer needs `A_X(chi)` itself to decay polynomially.

## 2. Munsch already proves the relevant squarefree-character theorem

`MC-055` obtained a fixed-comparator square-root power exponent by inserting Pólya--Vinogradov termwise into

\[
F_\chi(x)
=
\sum_{d\le\sqrt x}\mu(d)\chi(d^2)
\sum_{m\le x/d^2}\chi(m).
\tag{15}
\]

That was enough to expose the nonuniformity issue, but it is not the sharp classical prior-art boundary for the sum `(2)`.

Munsch's Lemma 2.3 studies exactly

\[
S_\chi^{\mathrm{free}}(x)
=
\sum_{n\le x}\mu(n)^2\chi(n)
\]

and proves two elementary character-sum bounds. The Burgess-based branch is `(4)`, while a Pólya--Vinogradov splitting gives a companion bound of shape

\[
|S_\chi^{\mathrm{free}}(x)|
\ll
x^{1/2}q^{1/4}(\log q)^{1/2}.
\tag{16}
\]

For prime `q`, the paper's Remark 2.4 replaces the `q^epsilon` loss in `(4)` by a square root of `log q`. At the power level relevant here, `(4)` is the stronger of these two certificates throughout the regime `q=X^kappa` with `1<=kappa<2`.

Consequently `(5)` is not a speculative estimate assembled for Mathia. It is the exact local-agreement transfer `(3)` coupled to an established theorem for the comparator class itself.

## 3. The `r=2` Burgess insertion is already optimal inside the direct fixed-r convolution scheme for `1<=kappa<=2`

The exponent `3/16` is not an arbitrary parameter choice. The classical fixed-`r` Burgess estimate anchored in `MC-S34` has the form

\[
\left|\sum_{m\le T}\chi(m)\right|
\ll_{r,\delta}
T^{1-1/r}q^{(r+1)/(4r^2)+\delta}.
\tag{17}
\]

Insert `(17)` absolutely into `(15)`. For `r=2`, the divisor sum is harmonic and gives

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16+\delta}\log X.
\tag{18}
\]

For every fixed `r>=3`, the divisor exponent is summable:

\[
\sum_{d\le\sqrt X}d^{-2+2/r}=O_r(1),
\]

so

\[
|F_\chi(X)|
\ll_{r,\delta}
X^{1-1/r}q^{(r+1)/(4r^2)+\delta}.
\tag{19}
\]

If `q<=X^kappa`, the power exponent in `(18)` is

\[
e_2(\kappa)=\frac12+\frac{3\kappa}{16},
\tag{20}
\]

while for `r>=3` it is

\[
e_r(\kappa)
=
1-\frac1r
+
\kappa\frac{r+1}{4r^2}.
\tag{21}
\]

For `r>=3`, the coefficient of `kappa` in `e_r-e_2` is negative, so on `1<=kappa<=2` the difference is minimized at `kappa=2`. There

\[
e_r(2)-e_2(2)
=
\frac{(r-2)^2}{8r^2}
>0.
\tag{22}
\]

Hence

\[
\boxed{e_2(\kappa)<e_r(\kappa)\quad(r>=3,\ 1\le\kappa\le2).}
\tag{23}
\]

So merely choosing a larger Burgess moment parameter does not remove the `11/16` floor. Beating it requires information not captured by absolute termwise insertion of the classical one-dimensional Burgess estimate into the square-divisor decomposition.

## 4. Exact exponent budget for a direct comparator proof

Suppose one tries to certify a target exponent `theta` using only `(5)`, ignoring logarithms at first order. The two terms require

\[
A_X(\chi)
\lesssim
X^{\theta-1},
\tag{24}
\]

and

\[
q
\lesssim
X^{\frac{16}{3}(\theta-1/2)}.
\tag{25}
\]

Equation `(25)` is compatible with `q>X` only if

\[
\theta>\frac{11}{16}
\]

(up to endpoint logarithms). Thus `(8)` is the first unavoidable power barrier of this particular certificate architecture.

The budgets become concrete away from the endpoint. For example, a direct `theta=3/4` certificate would need roughly

\[
A_X(\chi)\lesssim X^{-1/4},
\qquad
q\lesssim X^{4/3},
\tag{26}
\]

again up to logarithmic margins. These are much stronger requirements than the fixed defect condition used to derive the pairwise rigidity findings.

The distinction is useful for future searches. A quadratic character with a visibly small **constant** weighted defect can be mathematically interesting for repulsion, but it is not yet a Mertens transfer certificate. Conversely, a low-conductor character is insufficient unless its weighted defect decays at the polynomial rate required by `(24)`.

## 5. Coupling the transfer budget to the multiscale repulsion frontier

There is a further consequence when a direct certificate aims below exponent `7/8`. From `(25)`, a target

\[
\frac{11}{16}<\theta<\frac78
\tag{27}
\]

requires, with a small fixed margin to absorb logarithms,

\[
q\le X^\kappa
\qquad\text{for some fixed }\kappa<2.
\tag{28}
\]

At the same time `(24)` makes `A_X(chi)` tend to zero, so for all sufficiently large scales it lies below any fixed defect threshold `c<1/2`. Such successful certificates therefore enter the hypotheses of `MC-062` and `MC-063`.

This means a multiscale direct-transfer proof below `7/8` cannot freely choose a fresh prime-quadratic certificate at each nearby scale. Distinct successful conductor identities are power-separated, and only `O(log log T)` distinct identities can occur through scale `T` under one fixed subquadratic complexity exponent. The exact limiting turnover exponent from `MC-063` is

\[
\frac4\kappa-1,
\]

which is strictly larger than one when `(28)` holds.

For the illustrative `theta=3/4` budget `(26)`, one may take `kappa` just above `4/3`; the limiting turnover exponent is then just below `2`. Thus even a hypothetical three-quarter-power direct quadratic certificate would need long persistence of the same character or power-separated changes of identity. The local defect and the conductor cannot be optimized independently at every scale.

This does not prove that such certificates exist or that persistence itself gives Mertens cancellation. It only connects the classical one-certificate transfer budget to the already-proved multiscale repulsion cost.

## 6. Prior art and novelty boundary

The central analytic theorem is classical prior art: Marc Munsch, *Character sums over squarefree and squarefull numbers*, Archiv der Mathematik 102 (2014), 555--563, DOI `10.1007/s00013-014-0658-9`. Lemma 2.3 defines and estimates exactly the squarefree character sum used here. Its proof starts from the standard identity `mu^2(n)=sum_{d^2|n}mu(d)` and inserts Pólya--Vinogradov or Burgess; Remark 2.4 records the logarithmic improvement when the modulus is prime.

`MC-S34` already anchors the general Burgess estimate. A targeted search around squarefree character sums found Munsch's paper as direct prior art and later work on squarefree integers in residue classes and character-sum applications, but this audit does not claim that Lemma 2.3 is the optimal theorem known in every modulus/averaging regime. No novelty is claimed for the squarefree character sum, Burgess insertion, or the exponent `3/16` itself.

The retained Mathia content is the exact coupling of three already-audited pieces: the weighted Möbius-prime defect from `MC-060`--`MC-063`, the coefficientwise transfer `(3)`, and the classical squarefree-character bound `(4)`. Together they expose the quantitative defect/conductor budget and show precisely what the standard direct quadratic-comparator route can and cannot certify.

## 7. Boundaries and falsification tests

The conclusion is deliberately method-specific.

- The modulus is an odd prime `q>X` and `chi` is quadratic. Munsch's squarefree-character theorem is more general, but `(3)` uses the quadratic Möbius-sign setup of this line.
- Equation `(5)` is an upper bound. The fact that its right-hand side has an `11/16` power floor does **not** imply that `F_chi(X)` or `M(X)` is that large.
- The floor applies to the direct certificate that bounds the square-divisor expansion absolutely using classical one-dimensional Burgess estimates. It is not a no-go theorem against stronger signed, bilinear, averaged-family, spectral, or zero-density information.
- The fixed-defect good certificates of `MC-062`--`MC-063` do not by themselves yield a power saving through `(5)` because their transfer error `X A_X` may remain linear.
- Exact prefix interpolation has `A_X=0`, but `MC-057` shows that prime-quadratic exact interpolants already require at least quadratic conductor. That makes the classical comparator term worse, not better; it does not convert an upper-bound expression into a lower bound for the true sum.
- The multiscale consequence in Section 5 applies only when the intended certificate really obeys a fixed subquadratic conductor ceiling and eventually a fixed defect gap below `1/2`.

The main calculation is falsified if the coefficientwise inequality `(14)` fails, if Munsch's Lemma 2.3 does not apply to the nonprincipal prime character, or if the exponent comparison `(20)`--`(23)` is wrong. Each component is explicit and independently checkable.

## Consequence for the active frontier

The moving quadratic-comparator program now has a concrete quantitative objective rather than only a uniformity warning. A direct proof through a squarefree character comparator must jointly manufacture a polynomially vanishing weighted defect and a conductor small enough that the classical comparator theorem is useful at the same observation scale.

Classical Burgess technology inserted absolutely into the square-divisor decomposition bottoms out at exponent `11/16`, and any attempt below `7/8` simultaneously enters the subquadratic multiscale rigidity regime of `MC-062`--`MC-063`. The surviving route must therefore add genuinely new information: a stronger squarefree-character estimate uniform in the moving conductor, cancellation between square-divisor layers, a signed/bilinear coupling, or a different source-forced comparator whose cancellation theorem has a better complexity law. Reusing the standard fixed-character Burgess theorem more carefully does not reach the RH boundary.