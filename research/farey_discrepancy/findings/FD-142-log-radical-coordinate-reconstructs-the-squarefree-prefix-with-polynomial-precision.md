# FD-142 — Log-radical coordinate reconstructs the squarefree prefix with polynomial precision

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** main-track boundary theorem / information-capacity refinement
- **Depends on:** FD-135, FD-140, FD-141

## Claim

The `Theta(pi(T))` precision cost exhibited by the superincreasing coordinate in FD-141 is a cost of that particular encoding, not a lower bound for one-dimensional strongly additive reconstruction of the squarefree prefix.

There is a single fixed strongly additive coordinate

\[
L(n):=\sum_{p\mid n}\log p=\log\operatorname{rad}(n)
\tag{1}
\]

with the following properties.

1. On squarefree integers,

   \[
   L(n)=\log n,
   \tag{2}
   \]

   so `L` is injective on every squarefree prefix.
2. For distinct squarefree `m,n<=T`,

   \[
   |L(n)-L(m)|>\frac1T.
   \tag{3}
   \]

   Thus absolute precision of order `1/T` already suffices to distinguish every squarefree state through height `T`.
3. The explicit uniform quantization

   \[
   Q_T(n):=\left\lfloor 2T\,L(n)\right\rfloor
   \tag{4}
   \]

   is injective on squarefree `n<=T` and uses at most

   \[
   2T\log T+2
   \tag{5}
   \]

   values. Hence it can be stored using

   \[
   \log_2T+\log_2\log T+O(1)
   \tag{6}
   \]

   bits.
4. Any encoding that is injective on all squarefree integers through `T` needs at least

   \[
   \log_2 T-O(1)
   \tag{7}
   \]

   bits, already by an elementary linear lower bound for the number of squarefree integers. Therefore the uniform finite-precision realization of `L` is within an additive `O(log log T)` bits of the information-theoretic minimum, and an optimal coding of its discrete image uses `Theta(log T)` bits.

Consequently, neither **finite precision** nor even **polynomially small absolute precision** is by itself a noncircular admissibility condition for ancestry coordinates. A one-dimensional fixed strongly additive coordinate can reconstruct the whole squarefree source at essentially the ambient source-entropy scale `Theta(log T)` bits.

The useful post-FD-141 boundary is therefore sharper: an information-budget theorem must either stay genuinely below the `Theta(log T)` source-identity scale, constrain the effective alphabet/regularity in a way that forbids such source labeling, or derive the coordinate from the Farey/Franel/Fourier observable itself. This finding does not assert that any such restriction is sufficient for coercivity.

## 1. A fixed strongly additive coordinate

For every positive integer `n`, let

\[
\operatorname{rad}(n):=\prod_{p\mid n}p.
\tag{8}
\]

Define

\[
L(n):=\log\operatorname{rad}(n)
     =\sum_{p\mid n}\log p.
\tag{9}
\]

Then

\[
L(p^k)=\log p\qquad(k\ge1),
\tag{10}
\]

and, whenever `(m,n)=1`,

\[
L(mn)=L(m)+L(n).
\tag{11}
\]

Thus `L` is strongly additive in exactly the prime-support sense used by the ancestry coordinates of FD-138--FD-141.

If `n` is squarefree, then `rad(n)=n`, hence

\[
\boxed{L(n)=\log n.}
\tag{12}
\]

Therefore

\[
\mu^2(m)=\mu^2(n)=1,\qquad L(m)=L(n)
\quad\Longrightarrow\quad
m=n.
\tag{13}
\]

This is already complete squarefree source recovery. Unlike the superincreasing code of FD-141, the prime weights `log p` do not allocate an exponentially tiny private digit to each successive prime. They simply encode the radical multiplicatively.

## 2. The squarefree code has inverse-polynomial minimum spacing

Let

\[
\Delta_L(T):=
\min_{\substack{m\ne n\le T\\
                  \mu^2(m)=\mu^2(n)=1}}
|L(n)-L(m)|.
\tag{14}
\]

Take distinct positive integers `m<n<=T`. Since the logarithm is increasing,

\[
\log n-\log m
=\log\!\left(1+\frac{n-m}{m}\right)
\ge
\log\!\left(1+\frac1{T-1}\right).
\tag{15}
\]

For `x>0`,

\[
\log(1+x)>\frac{x}{1+x}.
\tag{16}
\]

Applying this with `x=1/(T-1)` gives

\[
\log\!\left(1+\frac1{T-1}\right)>\frac1T.
\tag{17}
\]

Because `L(k)=log k` on squarefree `k`, we obtain the uniform bound

\[
\boxed{\Delta_L(T)>\frac1T.}
\tag{18}
\]

The comparison with FD-141 is immediate. Its explicit superincreasing coordinate had minimum spacing

\[
\Delta_F(T)=\Theta(3^{-\pi(T)}),
\tag{19}
\]

whereas the fixed coordinate (9) has at least inverse-linear spacing on the same squarefree prefix. The earlier exponential precision tax is therefore not universal.

No claim is made that `1/T` is the exact minimum squarefree gap for every `T`; the lower bound is all that is needed for stable recovery.

## 3. An explicit finite-precision decoder

Define the quantized observation

\[
Q_T(n):=\lfloor 2T L(n)\rfloor.
\tag{20}
\]

Suppose that squarefree `m,n<=T` satisfy `Q_T(m)=Q_T(n)`. Two real numbers in the same half-open quantization cell of width `1/(2T)` differ by less than `1/(2T)`. Hence

\[
|L(n)-L(m)|<\frac1{2T},
\tag{21}
\]

contradicting (18) unless `m=n`. Therefore

\[
\boxed{
Q_T\text{ is injective on }\{n\le T:\mu^2(n)=1\}.
}
\tag{22}
\]

Equivalently, an observation of `L(n)` with deterministic absolute error below `1/(4T)` has disjoint uncertainty intervals for distinct squarefree `n<=T` and therefore determines `n` uniquely.

Since

\[
0\le L(n)\le\log T
\qquad(n\le T),
\tag{23}
\]

we also have

\[
0\le Q_T(n)\le 2T\log T.
\tag{24}
\]

Thus the complete squarefree source can be separated using at most

\[
2T\log T+2
\tag{25}
\]

uniform quantization symbols. A fixed-length binary representation therefore needs at most

\[
\boxed{
\log_2T+\log_2\log T+O(1)
}
\tag{26}
\]

bits.

This is a concrete finite-precision statement, not an exact-real loophole. The required absolute resolution is merely polynomial in the horizon.

## 4. The ambient source identity already costs `Theta(log T)` bits

The preceding upper bound is close to the minimum possible for any injective representation of the squarefree prefix.

Let

\[
S(T):=\#\{n\le T:\mu^2(n)=1\}.
\tag{27}
\]

An integer that is not squarefree is divisible by `m^2` for some integer `m>=2`. Hence, by the union bound,

\[
T-S(T)
\le
\sum_{2\le m\le\sqrt T}\left\lfloor\frac{T}{m^2}\right\rfloor
\le
T\sum_{m=2}^{\infty}\frac1{m^2}.
\tag{28}
\]

The elementary integral estimate

\[
\sum_{m=2}^{\infty}\frac1{m^2}
\le
\frac14+\int_2^\infty\frac{dx}{x^2}
=\frac34
\tag{29}
\]

gives

\[
\boxed{S(T)\ge\frac T4.}
\tag{30}
\]

Therefore every injective code on the squarefree prefix has at least `T/4` distinguishable outputs, and so requires at least

\[
\boxed{
\log_2 S(T)\ge\log_2T-2
}
\tag{31}
\]

bits.

Combining (26) and (31), the uniform quantization of `L` is within `O(log log T)` bits of the elementary information lower bound. If one encodes only the actual discrete image `L({n<=T:mu^2(n)=1})` rather than a uniform real grid, its resolving cardinality is exactly `S(T)`, so its intrinsic state-label cost is `Theta(log T)` bits.

The distinction matters. FD-141 correctly showed that coordinate dimension alone says nothing about capacity, but its particular coordinate made the precision budget much larger than the minimum needed to identify the source. The present coordinate shows that full reconstruction occurs already at essentially the ordinary bit complexity of the integer index itself.

## 5. Exact and quantized cells both destroy ancestry dilution

Let `p` be an active prime and let the parent domain contain squarefree `n<=T` with `p` not dividing `n`. Under exact conditioning on `L`, every nonempty cell contains one squarefree parent by (13).

The same remains true after the explicit quantization (20). For a quantized value `q`, let

\[
\mathcal C_{p,q}(T)
:=
\{n\le T:\mu^2(n)=1,\ p\nmid n,\ Q_T(n)=q\}.
\tag{32}
\]

By (22),

\[
|\mathcal C_{p,q}(T)|\le1.
\tag{33}
\]

Hence every conditional averaged ancestry defect over a nonempty such cell is exactly the pointwise edge defect. For example, for `1<=r<infinity`,

\[
\frac1{|\mathcal C_{p,q}(T)|}
\sum_{n\in\mathcal C_{p,q}(T)}|a_{pn}+a_n|^r
=
|a_{pn_q}+a_{n_q}|^r
\tag{34}
\]

when the cell is `{n_q}`.

Thus the hidden-wall constructions of FD-132--FD-140 cannot exploit conditional-density dilution once this much resolving information is supplied. But this is not a positive coercivity mechanism: the condition has already identified the parent integer. It has crossed into source reconstruction.

## 6. What this rules out

FD-141 established that arbitrary exact real coordinates are too expressive for a finite-dimensional incompleteness theorem. One possible repair was to demand finite precision, or perhaps only polynomially fine precision, hoping that a hidden prime-color wall would then reappear.

The coordinate `L` rules out that repair in this unrestricted form. It is fixed, one-dimensional and strongly additive; its squarefree values through `T` remain completely distinguishable after quantization at scale `Theta(1/T)`.

Therefore none of the following conditions alone can define a noncircular intermediate ancestry regime:

- a fixed number of real additive coordinates;
- finite precision at every finite horizon;
- inverse-polynomial absolute precision;
- an effective alphabet of order `T` up to polylogarithmic factors.

Each still permits complete labeling of the squarefree source.

A sublinear effective alphabet, for example `M_T=o(T)`, at least prevents injectivity on the entire squarefree prefix by (30). That is only a necessary non-reconstruction condition. It does **not** imply that some thin-wall source defeats the resulting ancestry averages, and it does not establish coefficient coercivity. Those are separate questions.

## 7. Relation to the Farey discrepancy problem

Nothing in the construction uses a new Farey identity. In fact, that is the point of the matched control.

The coordinate `L(n)=log rad(n)` is a direct source label on the squarefree fiber: there it is simply `log n`. It does not arise here from the Farey discrepancy field, the floor-quotient Fourier skeleton, a Vasyunin/Dedekind correlation, or a new geometric invariant. Using it as the decisive conditioning variable would therefore be circular if the goal were to recover the coefficient source from genuinely weaker Farey-visible information.

The consequence for the line is a restriction on what a useful positive theorem may assume. After FD-140--FD-142, an admissible information budget cannot be specified only by coordinate count and nominal numerical precision. It must distinguish **source-native information** from a compressed copy of the source index itself, or else quantitatively limit resolving capacity below the scale on which the squarefree prefix can be labeled.

A destination-side coercivity theorem on the Farey/Fourier skeleton remains logically different because it need not reconstruct individual coefficients at all.

## 8. Prior-art and novelty audit

The ingredients are classical and no novelty is claimed for them. The radical is the product of the distinct prime divisors, `log rad(n)=sum_(p|n) log p` is an immediate strongly additive identity, and on squarefree integers `rad(n)=n`. The spacing and coding estimates above are elementary consequences of monotonicity of `log` and counting.

A literature search around `log rad(n)`, strongly additive arithmetic functions, radical/abc notation, and finite information coding did not identify a theorem whose mathematical content is the present Mathia-specific boundary statement. The durable delta is therefore not a new arithmetic identity. It is the consequence for the FD-140--FD-141 information-capacity program: **the precision resource can fall from `Theta(pi(T))` bits in the superincreasing example to essentially `Theta(log T)` bits while retaining complete squarefree source recovery**.

Because no external theorem is load-bearing in the derivation, `SOURCES.md` requires no new anchor for this finding.

## 9. Adversarial audit

### A. Is `L` really strongly additive rather than merely a monotone label?

Yes. Equation (9) is a sum of fixed prime weights `log p` over the prime support, so (10)--(11) are exact. Its coincidence with `log n` occurs only after restricting to the squarefree fiber.

### B. Is the coordinate secretly horizon-dependent?

No. `L` is fixed once and for all. Only the finite-precision readout `Q_T` depends on the horizon, exactly as any statement about the precision needed to resolve states through height `T` must.

### C. Does the argument require prime factorization as an additional oracle?

Not for injectivity. The observed scalar value identifies at most one squarefree `n<=T`; once the source index is identified, its prime support is mathematically determined. Computational cost of factoring that recovered integer is not the information-capacity question studied here.

### D. Is `1/T` claimed to be the exact minimum spacing?

No. Equation (18) is a uniform lower bound inherited from the full integer grid. The squarefree subset can have larger local gaps. The bound is sufficient to prove inverse-polynomial stable injectivity.

### E. Does the bit lower bound use the prime number theorem or the exact squarefree density?

No. The elementary union bound (28)--(30) already gives a positive linear density lower bound and therefore `Omega(log T)` bits. The sharper classical density `6/pi^2` is unnecessary.

### F. Does an `o(T)` alphabet necessarily leave a prime-color wall of the type in FD-140?

No. Pigeonhole noninjectivity alone says only that some squarefree states collide. It does not control the geometry, mass or ancestry boundary of those collisions. No such stronger claim is made.

### G. Does polynomial precision make this a source-native Farey observable?

No. Precision and provenance are different resources. The coordinate succeeds because on the relevant fiber it is the source index in logarithmic coordinates. The result is a warning that a precision restriction without a source-native/non-reconstruction condition remains circular.

### H. Does this improve the Franel--Landau bound or advance RH directly?

No. This is a boundary theorem for the coefficient-ancestry route. It removes an over-broad candidate notion of admissibility and narrows the next theorem to genuinely weaker information channels.

## Conclusion

Full squarefree source recovery does not require the exponentially fine prime-index digits used in FD-141. The fixed strongly additive coordinate

\[
L(n)=\log\operatorname{rad}(n)
\]

coincides with `log n` on squarefree integers, has minimum spacing greater than `1/T` through height `T`, and remains injective after a uniform quantization using only

\[
\log_2T+\log_2\log T+O(1)
\]

bits. Any injective representation already needs `Omega(log T)` bits, so this is near the ambient information floor.

The post-FD-141 frontier is therefore not merely **infinite precision versus finite precision**. It is **genuinely sub-source information versus enough resolving capacity to label the source**. A useful Farey-side coercivity law must live on the former side without smuggling in the latter.