# RE-013 — clean selector has a logarithmic prime-layer resolution barrier

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + FIXED-LAYER-FRONTIER-ASYMPTOTIC + FIXED-DEPTH-NONRESOLUTION + TWO-ADIC-DEPTH-BARRIER + LOGARITHMIC-RESOLUTION-SCALE + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-006` shows that a clean regular self-tangent CA local peak is selected inside a prime gap by the exact higher-layer mass

\[
\Phi_{\ge2}(X)
=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\
                  \eta_{r,j}\le X}}\log r,
\qquad X=\log C,
\]

through

\[
X-p=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr),
\qquad p<X<q.
\tag{1}
\]

The admissible clean-peak window in `RE-006` has width on the **logarithmic scale**. `RE-007` extracts the dominant second layer

\[
\Phi_2(X)=\sqrt{2X}+o(\sqrt X),
\]

which is enough for its square-root dichotomy but deliberately too coarse for (1). The natural next question is whether adding finitely many further prime-power layers repairs that loss. It does not.

For each fixed layer `j>=2`, let

\[
\Phi_j(X)
:=\sum_{\substack{r\ \mathrm{prime}\\\eta_{r,j}\le X}}\log r.
\tag{2}
\]

Then

\[
\boxed{
\Phi_j(X)=(jX)^{1/j}(1+o(1))
\qquad(j\ \text{fixed}).
}
\tag{3}
\]

Consequently, for every fixed truncation depth `J>=2`, the omitted selector mass

\[
R_J(X)
:=\Phi_{\ge2}(X)-\sum_{j=2}^{J}\Phi_j(X)
\tag{4}
\]

satisfies

\[
\boxed{
R_J(X)\ge\Phi_{J+1}(X)
=((J+1)X)^{1/(J+1)}(1+o(1))
\gg\log X.
}
\tag{5}
\]

Thus **no fixed finite prime-layer frontier can determine the clean CA selector at the resolution consumed by `RE-006`**.

There is a sharper variable-depth statement. The prime `2` alone forces logarithmically many active layers. If

\[
j_2(X):=\max\{j\ge2:\eta_{2,j}\le X\},
\tag{6}
\]

then

\[
\boxed{
 j_2(X)=\frac{\log(X\log X)}{\log2}+O(1).
}
\tag{7}
\]

Hence every truncation `J<j_2(X)` obeys

\[
\boxed{
R_J(X)
\ge
\log X+\log\log X-J\log2+O(1).
}
\tag{8}
\]

In particular, if `J=o(log X)`, the omitted mass is at least `(1-o(1))log X`; and if for fixed `delta>0`

\[
J\le(1-\delta)\frac{\log X}{\log2},
\]

then

\[
R_J(X)\ge\delta\log X+\log\log X+O(1).
\tag{9}
\]

This lower barrier is essentially sharp. Put

\[
J_X:=\left\lfloor\frac{\log X}{\log2}\right\rfloor.
\tag{10}
\]

For all sufficiently large `X`, **no prime `r>=3` has an active layer `j>J_X`**. Therefore the entire remaining tail comes from the prime `2`, and

\[
\boxed{
R_{J_X}(X)
=(j_2(X)-J_X)\log2
=\log\log X+O(1)
=o(\log X).
}
\tag{11}
\]

So `Theta(log X)` layer depth is the sharp scale, up to constant factors, for compressing the exact higher-layer selector below its natural logarithmic window. This is a resolution theorem about the source selector, not a new estimate for the mixed prime race and not a route around the global RH-equivalence obstruction of `RE-009`.

## 1. Every fixed prime-power layer has its own polynomial frontier

Retain the exact event definition from `RE-001`--`RE-007`. For a prime `r` and layer `j>=1`,

\[
\lambda_{r,j}
:=\log\frac{1-r^{-(j+1)}}{1-r^{-j}},
\qquad
\frac1{\eta_{r,j}\log\eta_{r,j}}
=\frac{\lambda_{r,j}}{\log r}.
\tag{12}
\]

The abundance increment can be written exactly as

\[
\lambda_{r,j}
=\log\!\left(
1+\frac{r-1}{r(r^j-1)}
\right).
\tag{13}
\]

For fixed `j` and `r->infinity`, the fraction inside the logarithm is

\[
\frac{r-1}{r(r^j-1)}
=r^{-j}(1+O(r^{-1})),
\]

and hence

\[
\boxed{
\lambda_{r,j}=r^{-j}(1+O(r^{-1})).
}
\tag{14}
\]

The event condition `eta_(r,j)<=X` is equivalent, because `x mapsto 1/(x log x)` decreases, to

\[
\frac{\lambda_{r,j}}{\log r}
\ge\frac1{X\log X}.
\tag{15}
\]

Using (14), the boundary prime `y_j(X)` for one fixed layer therefore satisfies

\[
y_j(X)^j\log y_j(X)
=X\log X\,(1+o(1)).
\tag{16}
\]

Since `log y_j(X)=(1/j)log X+O(1)`, this gives

\[
\boxed{
y_j(X)=(jX)^{1/j}(1+o(1)).}
\tag{17}
\]

The prime number theorem `vartheta(y)~y` then gives (3):

\[
\Phi_j(X)=\vartheta(y_j(X))+o(y_j(X))
=(jX)^{1/j}(1+o(1)).
\]

For `j=2`, this recovers the `sqrt(2X)` frontier used in `RE-007`. For `j=3`, the next omitted layer already has mass of order `X^(1/3)`, and similarly at every fixed depth.

Equation (5) now follows simply from positivity: `R_J` contains the whole `(J+1)`st layer. Since every positive power of `X` dominates `log X`, adding any fixed number of layers cannot approximate the selector at the logarithmic resolution required by (1).

## 2. The prime `2` forces logarithmically many active layers

The fixed-`j` asymptotic above must **not** be used when `j` grows with `X`. The depth barrier can instead be proved directly from the exact `r=2` increment. Equation (13) becomes

\[
\lambda_{2,j}
=\log\!\left(1+\frac1{2(2^j-1)}\right).
\tag{18}
\]

Put

\[
u_j:=\frac1{2(2^j-1)}.
\]

For `j>=2`,

\[
2^{-(j+1)}<u_j\le2^{-j},
\qquad u_j\le\frac16.
\tag{19}
\]

Using `u/(1+u)<=log(1+u)<=u`,

\[
\boxed{
\frac37\,2^{-j}
<\lambda_{2,j}
\le2^{-j}
\qquad(j\ge2).
}
\tag{20}
\]

A layer is active at `X` exactly when

\[
\lambda_{2,j}
\ge\frac{\log2}{X\log X}.
\tag{21}
\]

The two bounds in (20) sandwich the last active index between two logarithms differing only by an absolute constant. Therefore

\[
j_2(X)
=\log_2(X\log X)+O(1),
\]

which is (7).

Every active layer of the prime `2` contributes exactly `log2` to `Phi_(>=2)`. Hence, whenever `J<j_2(X)`, the omitted `2`-adic layers alone contribute

\[
(j_2(X)-J)\log2.
\]

Substitution of (7) proves (8), and the two displayed consequences (9) follow immediately. No prime-distribution theorem enters this lower bound; it comes from one fixed prime and the exact CA layer thresholds.

## 3. Depth `log_2 X` reduces the whole omitted selector to `log log X`

The lower bound becomes a matching resolution statement because deeper layers of every prime except `2` disappear by depth `J_X` in (10).

From (13) and `log(1+u)<=u`, one has for every prime and every `j>=1`

\[
\lambda_{r,j}\le r^{-j}.
\tag{22}
\]

If the layer `(r,j)` is active at `X`, (15) and (22) imply

\[
\boxed{
r^j\log r\le X\log X.}
\tag{23}
\]

Now suppose `r>=3` and `j>J_X`. Since `j>log_2 X`,

\[
r^j\log r
\ge3^j\log3
> X^{\log3/\log2}\log3.
\tag{24}
\]

Because `log3/log2>1`, the right side eventually exceeds `X log X`, contradicting (23). Thus for sufficiently large `X`, every active layer above `J_X` belongs to `r=2`.

The active `2`-layers are consecutive in `j`, since `lambda_(2,j)` decreases with `j`. Hence the tail after `J_X` is **exactly**

\[
R_{J_X}(X)
=(j_2(X)-J_X)\log2.
\tag{25}
\]

Using (7) and the bounded floor error in (10),

\[
(j_2(X)-J_X)\log2
=\log\log X+O(1),
\]

which proves (11).

This identifies a genuine compression boundary. To obtain an `o(log X)` approximation to `Phi_(>=2)(X)`, logarithmically many prime-power layers are both necessary, in the sense of (8)--(9), and sufficient, via (11). The dominant obstruction at the final depths is not a cloud of large primes but the long tower of exponent layers of the smallest prime.

## 4. Why this matters after the local-jet closure

`RE-012` proves that once the exact selector `(X,Phi_(>=2)(X))` is known, the entire smooth mixed-race profile inside the surrounding prime-free chamber is determined by one value `mathscr Y(X)` plus that selector. This makes a natural compression attempt attractive: replace the exact higher-layer mass by a finite prime-frontier expansion and hope that local value/slope data recovers the missing correction.

Equations (5) and (8) rule out that shortcut at fixed depth. The missing selector mass is larger than the complete logarithmic clean-peak window, so treating it as a lower-order error changes which coordinates qualify as self-tangent clean peaks. Any apparent new constraint recovered from derivatives after such a truncation can simply be information about the selector mass that the truncation discarded; it is not an independent arithmetic observable.

Equation (11) also gives the positive boundary of this negative result. A depth growing like `log_2 X` compresses the selector to `o(log X)` error. That may be enough for coarse mean-gap-scale questions, but it does **not** reproduce the additive `o(1)` resolution in the sharp window of `RE-006`: `log log X` still diverges. Therefore (11) should not be promoted into an exact finite-dimensional replacement for the self-tangent selector.

The second-layer normal form of `RE-007` remains useful. It operates at the square-root scale, where the omitted `O(X^(1/3) polylog X)` mass is negligible. The present result only says that the same finite-depth truncation cannot subsequently be reused as though it were accurate on the much smaller logarithmic selector scale.

## 5. Prior art and novelty boundary

The individual ingredients are classical or already represented in this line's sources. Alaoglu--Erdos supplies the CA exponent-threshold framework; the exact event normalization and prime-layer workload are closest to Mantovanelli's August 2026 preprint; the prime number theorem converts one fixed layer's boundary prime into its weighted mass. No novelty is claimed for the fact that a prime may carry many exponent layers, for the asymptotic size of CA exponents, or for the already-known square-root prime frontier.

A targeted audit of the current CA/Robin source record did not identify the specific resolution statement (5), (8), and (11): after the exact clean selector of `RE-006` is exposed, fixed layer depth is quantitatively incapable of reaching its logarithmic window, while `Theta(log X)` depth is the first scale at which the omitted mass becomes `o(log X)`. This should be read as a Mathia-specific consequence of combining the exact selector with classical layer thresholds, not as a blanket novelty claim about colossally abundant numbers.

No new source anchor is required. The non-elementary ingredients used here are already recorded in `SOURCES.md`, and the variable-depth lower/upper barrier is elementary once (12) is admitted.

## 6. Falsification boundaries and research consequence

Several quantifiers are load-bearing. Equation (3) is a **fixed-layer** asymptotic; it is not uniform in `j`, and using it with `j~log X` would be unjustified. The logarithmic-depth statements instead use the exact `2`-adic formula and the universal inequality (23). Conversely, the lower bound (8) does not assert that the prime `2` dominates the selector at shallow depths; it only supplies enough unavoidable omitted mass to establish the resolution barrier.

The result is also scale-specific. Fixed depth fails for the logarithmic clean selector but can still capture square-root-scale information, exactly as `RE-007` demonstrates. Depth `J_X` gives `O(log log X)` tail, not `O(1)` or an exact selector. No conclusion is drawn about how much deeper one must go for additive-unit resolution.

Most importantly, this finding does not bound the selected mixed race `mathscr Y`, prove that high mixed-race values avoid self-tangent coordinates, or control the exceptional higher-layer/tied boundary chamber of `RE-004`. It therefore does not prove Robin's inequality or RH.

Its durable effect is to close another finite-compression escape after `RE-012`. The nonlocal CA selector is itself a multiscale object whose logarithmic-resolution content requires a growing hierarchy of prime-power layers. A future selected-race theorem may use a compressed selector, but if it operates at the clean `O(log X)` window it must retain at least logarithmic layer depth, or supply an independent theorem controlling the discarded mass. Treating any fixed prime-frontier depth as the full source-selection state is now quantitatively falsified.