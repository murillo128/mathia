# MC-323 — Varying-modulus prime Halász–Montgomery forces quadratic source saturation

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the localized prime-shell/source-character setup of `MC-293`–`MC-322`. Let

\[
\mathcal A_y\subset\{p:y<p\le 2y\}
\]

be a dense prime shell with

\[
A_y:=|\mathcal A_y|\asymp \frac{y}{\log y},
\tag{1}
\]

and let `Xi` be a finite set of distinct Dirichlet characters `chi` whose individual moduli `q_chi` are cubefree and satisfy

\[
q_\chi\le Q.
\tag{2}
\]

Define the normalized prime-shell bias

\[
\beta_\chi
:=\frac1{A_y}\sum_{p\in\mathcal A_y}\chi(p),
\qquad
E_y(\Xi):=\sum_{\chi\in\Xi}|\beta_\chi|^2.
\tag{3}
\]

Jan-Christoph Schlage-Puchta's Theorem 3 in *Primes in short arithmetic progressions* contains a varying-modulus clause that is stronger for the present purpose than the fixed-modulus specialization used in `MC-321`–`MC-322`: if the characters have possibly different moduli `q_chi<=Q`, the same prime Halász–Montgomery estimate holds with the fixed modulus `q` replaced by `Q^2`; when all occurring moduli are cubefree, the Burgess parameter `k>=2` may be chosen arbitrarily.

Consequently, for every fixed `delta in (0,2)` there are constants `c_delta>0` and `C_delta>0` such that, whenever

\[
Q\le y^{2-\delta},
\tag{4}
\]

one has

\[
\boxed{
E_y(\Xi)
\le
C_\delta\left(1+|\Xi|\,y^{-c_\delta}\log y\right).
}
\tag{5}
\]

One may take, non-optimally, `k>=4/delta` fixed and

\[
c_\delta=\frac1{2k^2}
\tag{6}
\]

after the parameter choices in Section 2 below. Thus if `|Xi|=y^{o(1)}`, then

\[
\boxed{E_y(\Xi)=O_\delta(1).}
\tag{7}
\]

More pointedly, if `tau>0` is fixed, then for all sufficiently large `y`

\[
\boxed{
\#\{\chi:q_\chi\le y^{2-\delta},\ |\beta_\chi|\ge\tau\}
=O_\delta(\tau^{-2}).
}
\tag{8}
\]

This removes the **common-modulus hypothesis** from the fixed-bias obstruction throughout every fixed subquadratic individual-conductor range.

Apply `(8)` to the exact reciprocal endpoint partition of `MC-296`. For its `R` independent generator functionals `lambda_1,...,lambda_R` with equal defects `1/R`,

\[
x_{\lambda_i}= -\left(1-\frac2R\right),
\tag{9}
\]

so `|x_{lambda_i}|>=1/2` for `R>=4`. As in `MC-301`–`MC-302`, choose for each generator a minimizing lower-prime representative. It gives a distinct primitive real character `chi_i` of odd squarefree — hence cubefree — conductor

\[
q_i=\mathcal Q(\lambda_i),
\qquad
\beta_{\chi_i}=x_{\lambda_i}.
\tag{10}
\]

Therefore for every fixed `delta>0`,

\[
\boxed{
\#\{1\le i\le R:\mathcal Q(\lambda_i)\le y^{2-\delta}\}
=O_\delta(1).
}
\tag{11}
\]

Equivalently, if `R->infinity`, then **all but `O_delta(1)` endpoint generator directions require primitive source conductor exceeding `y^(2-delta)`**. This is stronger than the linear individual-conductor horizon of the quadratic-large-sieve obstruction in `MC-302`, and it does not embed the family into one common modulus before applying the analytic theorem.

There is a sharp consequence for the natural common source package used in `MC-312`–`MC-321`. Suppose its `n=2R` lower-prime source coordinates have common squarefree radical

\[
P=\prod_{u\in U}u,
\tag{12}
\]

and the exact-natural-scale cap

\[
Z:=\max U\le y^{1/R}.
\tag{13}
\]

Every generator has a package representative whose conductor divides `P`, so `(11)` implies, for every fixed `delta>0`,

\[
P>y^{2-\delta}
\tag{14}
\]

for all sufficiently large `R`. On the other hand `(12)`–`(13)` give

\[
P\le Z^{2R}\le y^2.
\tag{15}
\]

Hence any arithmetic realization of the exact endpoint law inside this natural package must satisfy the quadratic saturation law

\[
\boxed{
\frac{\log P}{\log y}\longrightarrow 2,
\qquad
P=y^{2-o(1)}.
}
\tag{16}
\]

The saturation is coordinatewise in density as well. For every fixed `eta>0`, all but `o(R)` of the `2R` source primes must obey

\[
\boxed{
u>y^{(1-\eta)/R}.}
\tag{17}
\]

Indeed, each source prime is at most `y^(1/R)`, while `(16)` says the total logarithmic deficit from the maximal product `y^2` is `o(log y)`; each coordinate violating `(17)` contributes at least `eta log y/R` of deficit.

Thus the common-modulus-free escape left after `MC-322` is not available at ordinary subquadratic source cost. The exact reciprocal endpoint can survive this classical prime-family estimate only by pushing essentially every generator to near-quadratic primitive conductor and, under the natural `2R`-coordinate package, by saturating the whole source radical and almost all source-coordinate scales. No estimate for `M(x)` follows.

## 1. The primary theorem has a varying-modulus clause

Schlage-Puchta's Theorem 3 states, in the notation of that paper, that for a set `C` of characters modulo one `q`, prime-supported coefficients `a_p`, sieve parameter `B`, and `k=2,3` — or arbitrary fixed `k>=2` when `q` is cubefree —

\[
\sum_{\chi\in C}
\left|\sum_{p\le N}a_p\chi(p)\right|^2
\le
\left(
\frac{N}{\log B}
+c_{k,\varepsilon}
N^{1-1/k}
q^{(k+1)/(4k^2)+\varepsilon}
|C|B^{2/k}
\right)
\sum_{p\le N}|a_p|^2.
\tag{18}
\]

Immediately after the displayed bounds, the theorem adds that if `C` consists of characters to **different moduli** `q<=Q`, the same estimates hold with `q` replaced by `Q^2`; moreover `k` remains arbitrary when all occurring moduli are cubefree. Thus `(18)` becomes

\[
\sum_{\chi\in C}
\left|\sum_{p\le N}a_p\chi(p)\right|^2
\le
\left(
\frac{N}{\log B}
+c_{k,\varepsilon}
N^{1-1/k}
Q^{(k+1)/(2k^2)+2\varepsilon}
|C|B^{2/k}
\right)
\sum_{p\le N}|a_p|^2.
\tag{19}
\]

This clause is load-bearing. The later Klurman–Mangerel–Teräväinen formulation used in `MC-321`–`MC-322` records a fixed-modulus version with `k in {2,3}`; it cites Schlage-Puchta for the underlying estimate but does not expose the full varying-modulus/cubefree-`k` flexibility needed here.

## 2. Normalization gives a fixed-subquadratic energy cap

Apply `(19)` with `N=2y` and

\[
a_p=1_{p\in\mathcal A_y}.
\]

Then `sum |a_p|^2=A_y`, and division by `A_y^2` together with `(1)` gives

\[
E_y(\Xi)
\ll
\frac{\log y}{\log B}
+
 y^{-1/k}
 Q^{(k+1)/(2k^2)+2\varepsilon}
 |\Xi|B^{2/k}\log y.
\tag{20}
\]

Fix `delta in (0,2)` and choose an integer

\[
k\ge \frac4\delta.
\tag{21}
\]

The exponent contributed by the first three power terms in the second summand of `(20)`, before the `epsilon` and `B` losses, is

\[
-\frac1k
+(2-\delta)\frac{k+1}{2k^2}
=
\frac{2-\delta(k+1)}{2k^2}
\le -\frac1{k^2}.
\tag{22}
\]

Now fix

\[
\varepsilon=\frac1{16k^2},
\qquad
B=\left\lfloor y^{1/(8k)}\right\rfloor.
\tag{23}
\]

For sufficiently large `y`, this is an admissible sieve parameter. From `Q<=y^(2-delta)`,

\[
Q^{2\varepsilon}
\le y^{1/(4k^2)},
\qquad
B^{2/k}\le y^{1/(4k^2)}.
\tag{24}
\]

Combining `(22)`–`(24)` gives a net power at most

\[
y^{-1/(2k^2)}.
\tag{25}
\]

Also

\[
\frac{\log y}{\log B}=O(k)=O_\delta(1).
\tag{26}
\]

Equations `(20)`, `(25)`, and `(26)` prove `(5)`–`(7)` with the non-optimized choice `(6)`.

For `(8)`, let `m_tau` be the number of selected characters with `|beta_chi|>=tau`. Applying `(5)` only to that subfamily gives

\[
m_\tau\tau^2
\le
C_\delta\left(1+m_\tau y^{-c_\delta}\log y\right).
\tag{27}
\]

For fixed `tau`, the coefficient `C_delta y^(-c_delta) log y` is eventually at most `tau^2/2`, so it can be absorbed into the left side. This proves `m_tau=O_delta(tau^-2)`.

## 3. Exact endpoint bias converts the family bound into conductor saturation

The equal-defect endpoint law is already exact in `MC-296`: for every subset `I` of the `R` independent generators,

\[
x_{\lambda_I}
=(-1)^{|I|}\left(1-\frac{2|I|}{R}\right).
\tag{28}
\]

Taking singleton subsets gives `(9)`. The primitive source-character dictionary is already established in `MC-301`–`MC-302`: a minimizing squarefree lower-prime representative of a nonzero shell functional yields a primitive real character, distinct functionals yield distinct characters, and its prime-shell average is the corresponding `x_lambda`.

Fix `delta>0` and apply `(8)` with `tau=1/2` to the subfamily of generator characters satisfying `Q(lambda_i)<=y^(2-delta)`. All hypotheses hold: their primitive conductors are odd and squarefree, the characters are distinct, and their biases have magnitude at least one half. This proves `(11)`.

For the natural package, if `q_i^pkg` is the conductor of the package representative of `lambda_i`, then

\[
\mathcal Q(\lambda_i)\le q_i^{pkg}\mid P.
\tag{29}
\]

Since `(11)` leaves at most `O_delta(1)` low-conductor generators while `R->infinity`, at least one generator has `Q(lambda_i)>y^(2-delta)`, and then `(29)` forces `(14)`. As `delta>0` was arbitrary but fixed, `(14)` together with `(15)` yields `(16)`.

Finally write the `2R` source primes as `u_1,...,u_(2R)`. From `(13)`,

\[
0\le \frac{\log y}{R}-\log u_j.
\]

Summing and using `(16)` gives

\[
\sum_{j=1}^{2R}
\left(\frac{\log y}{R}-\log u_j\right)
=2\log y-\log P
=o(\log y).
\tag{30}
\]

Every `u_j<=y^((1-eta)/R)` contributes at least `eta log y/R` to `(30)`, so the number of such coordinates is `o(R)`. This proves `(17)`.

## 4. Prior art and novelty boundary

The analytic input is classical. The primary source is Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143–149, DOI `10.4064/aa106-2-4`, especially Theorem 3. The publisher's scan states explicitly that for characters to different moduli `q<=Q`, the theorem remains valid with `q` replaced by `Q^2`, and that arbitrary `k` is available when all those moduli are cubefree.

The modern source already retained as `MC-S45`, Oleksiy Klurman, Alexander P. Mangerel and Joni Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proceedings of the London Mathematical Society **127** (2023), 366–446, uses Schlage-Puchta's theorem in its prime Halász–Montgomery machinery. The fixed-modulus specialization underlying `MC-321`–`MC-322` is therefore not a different analytic mechanism.

No novelty is claimed for Schlage-Puchta's inequality, the Burgess exponent, or prime Halász–Montgomery. The durable delta here is the exact composition of the **published varying-modulus cubefree clause** with the reciprocal endpoint source-character dictionary from `MC-296`, `MC-301`–`MC-302`, and the natural source-package ceiling from `MC-312`–`MC-321`. That composition closes a previously explicit Mathia escape route: abandoning a common-modulus embedding no longer permits fixed-bias endpoint generators at any fixed subquadratic primitive-conductor exponent.

## Boundaries and falsification tests

- **Cubefree individual moduli are load-bearing for arbitrary `k`.** The endpoint source characters satisfy this because their minimizing primitive real conductors are odd squarefree. Without cubefreeness, Schlage-Puchta permits only `k=2,3`, and the near-quadratic conclusion does not follow from this argument.
- **The exponent gap is fixed.** The theorem is applied for each fixed `delta>0` with fixed `k=k(delta)` and fixed `epsilon`. Nothing here is uniform enough to put `delta=delta(y)->0` inside the analytic estimate. The notation `y^(2-o(1))` in `(16)` follows only after quantifying over every fixed `delta` and combining with the independent upper bound `P<=y^2`.
- **Dense prime support is load-bearing.** The normalization `(20)` uses `A_y asymp y/log y`. A sparse shell or a different support geometry has a different energy budget.
- **Distinct characters are load-bearing.** Independence of the endpoint generators supplies distinct shell functionals, and the source-character dictionary of `MC-301` makes the selected primitive characters distinct. Repeated copies cannot be counted as new directions.
- **Fixed endpoint bias is load-bearing.** The strong conductor count `(11)` uses `|x_(lambda_i)|>=1/2`. A model whose individual generator biases decay with `R` must be compared to `(5)` at that actual threshold.
- **Quadratic radical saturation uses the natural package.** Equations `(14)`–`(17)` additionally require a common source package containing representatives of all generator directions, `n=2R`, and `Z<=y^(1/R)`. The varying-modulus energy bound `(5)` itself does not require a common radical.
- **No exact quadratic-boundary theorem is claimed.** The argument rules out every fixed exponent `2-delta`; it does not prove a useful estimate at `Q=y^2`, where the optimized fixed-parameter power saving disappears.
- **No Möbius endpoint realization is asserted.** The result is conditional on the exact reciprocal endpoint source geometry. It is a no-go/capacity theorem for that candidate mechanism, not evidence that Möbius itself realizes the endpoint model.
- **No Mertens or RH estimate follows.** The result further narrows one source-character mechanism but gives no bound on `M(x)` and imports no zero-free statement for `zeta(s)`.