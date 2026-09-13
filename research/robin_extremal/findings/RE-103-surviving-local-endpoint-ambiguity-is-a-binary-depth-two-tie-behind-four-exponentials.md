# RE-103 — surviving local endpoint ambiguity is a binary depth-two tie behind four exponentials

**Status:** `EXACT-DERIVED + FRONTIER-SYNTHESIS + BINARY-DEPTH2-ENDPOINT-NORMAL-FORM + DEFORMED-QUADRATIC-PRIME-HIT + FOUR-EXPONENTIALS-BOUNDARY + GLOBAL-ASSEMBLY-SEPARATION + PRIOR-ART-AUDITED`.

`RE-102` closes the current local support-boundary depth hierarchy above

\[
\Theta_*:=\frac{265657}{307200}=0.8647688802\ldots
\tag{1}
\]

but deliberately leaves endpoint ties unresolved. Combining its two-sided first-layer-contact conclusion with the deep-boundary exceptional-set removal from `RE-091`, the classical Alaoglu--Erdos prime-or-distinct-semiprime transition theorem already packaged in `RE-004`, and the deformed quadratic event map of `RE-096` gives a much smaller residual local normal form.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho,
\qquad
\Theta>\Theta_*,
\tag{2}
\]

and choose

\[
J\Subset(1-\Theta,1-\Theta_*).
\tag{3}
\]

On sufficiently late common positive CA blocks, outside a union of selected threshold cells of total `J`-measure `o_J(1)`, every adjacent physical support boundary of every surviving selected cell has **exactly one of two forms**:

\[
\boxed{
\{(p,1)\}
\quad\text{or}\quad
\{(p,1),(q,2)\},
}
\tag{4}
\]

where `p,q` are distinct ordinary primes. Thus every surviving local chamber is an ordinary consecutive-prime gap from `RE-102` with at most one **binary depth-two decoration** on each endpoint. No depth `j\ge3` co-event and no second additional event survives on this full-measure threshold set.

If the decoration is present, it satisfies the exact incidence

\[
\boxed{
\eta_1(p)=\eta_2(q)
\iff
p=x(q):=\eta_1^{-1}(\eta_2(q)),
}
\tag{5}
\]

so `RE-096` gives

\[
\boxed{
 p
 =\frac{q^2}{2}
 \left(
 1+\frac{\log2}{2\log q}
 +\frac{\log2(\log2-1)}{4(\log q)^2}
 +O((\log q)^{-3})
 \right).
}
\tag{6}
\]

Equivalently,

\[
q=\sqrt{2p}\left(1+O((\log p)^{-1})\right).
\tag{7}
\]

The physical CA transition quotient at such a boundary is therefore either `p` or `pq`; in the tied case

\[
\boxed{
 pq=\sqrt2\,p^{3/2}
 \left(1+O((\log p)^{-1})\right),
\qquad
\log(pq)=\frac32\log p+\frac12\log2+O((\log p)^{-1}).
}
\tag{8}
\]

The residual tie channel is not merely a difficult prime-pattern problem. Every actual two-prime tie produces exactly the Alaoglu--Erdos special-case obstruction to the **Four Exponentials conjecture**. Hence, conditionally on Four Exponentials, the second alternative in (4) never occurs and almost every selected local chamber above (1) has two **simple, untied first-layer endpoints**. Unconditionally, eliminating those ties in isolation would settle a classical open transcendence special case, so the current Robin program should not treat local tie removal as an ordinary remaining short-interval estimate.

## 1. The RE-102 good set leaves only depth two at a first-layer endpoint

`RE-102` constructs exceptional unions `\mathcal E_{\mathcal B}\subset J` with

\[
|\mathcal E_{\mathcal B}|\to0
\tag{9}
\]

along late blocks, such that every selected cell outside them has first-layer contact on **both** adjacent physical support boundaries. Its exceptional union explicitly contains the depth-at-least-three boundary set from `RE-091`. Therefore, after enlarging the exceptional union by another `o_J(1)` set if necessary, a surviving boundary coordinate `\xi` satisfies

\[
\xi=\eta_1(p)
\tag{10}
\]

for one ordinary prime `p`, and contains no event `(r,j)` with `j\ge3`.

Two distinct first-layer events cannot tie because `p\mapsto\eta_1(p)` is strictly increasing (`RE-004`). Thus any additional event at `\xi` must have depth exactly `2`.

The classical Alaoglu--Erdos transition theorem used in `RE-004` says that a consecutive physical CA quotient is either one prime or the product of two **distinct** primes; in event language, a physical transition coordinate cannot carry three distinct prime-factor increments and cannot carry the square of one prime. Since (10) already supplies one first-layer event, at most one depth-two co-event can remain. This proves the exhaustive local classification (4).

This is stronger than the transition-count statement of `RE-004` only because it is conditioned on the selected false-RH threshold geometry developed later in the line. No novelty is claimed for the prime-or-semiprime theorem itself.

## 2. A surviving tie is an exact prime hit on the RE-096 deformation

For real `t>1`, `RE-096` defines

\[
x(t):=\eta_1^{-1}(\eta_2(t)).
\tag{11}
\]

Hence a surviving co-event `(p,1),(q,2)` obeys (5) tautologically. The expansion (6) is exactly `RE-096` evaluated at the prime host `q`; no short-interval approximation is being used. In particular the tied channel asks for an **exact prime value** of the deformed quadratic sequence `x(q)`, not merely for a prime in a neighborhood of `x(q)`.

This distinction matters for the previous sparse-host argument. `RE-095`--`RE-101` eliminate cells whose depth-two-only endpoint forces a prime-free neighborhood around `x(q)`. A tie is the opposite extreme: there is a prime at the sample point itself. The successful short-interval exceptional-set machinery therefore does not become stronger by iteration here; it has already solved a different, coarse incidence problem.

Equation (7) follows by inverting the leading term in (6), and (8) follows immediately. Thus the only higher-layer information that can remain on a typical local support endpoint is a single bit together with an extremely rigid factor scale: an optional depth-two prime of size `\asymp p^{1/2}` attached to the first-layer prime of size `\asymp p`.

## 3. Every binary tie is a Four-Exponentials counterexample

Use the exact event notation

\[
g(X)=\frac1{X\log X},
\qquad
\lambda_j(r)
=\log\frac{1-r^{-(j+1)}}{1-r^{-j}},
\qquad
 g(\eta_j(r))=\frac{\lambda_j(r)}{\log r}.
\tag{12}
\]

Suppose

\[
\eta_1(p)=\eta_2(q)=\xi
\tag{13}
\]

for distinct primes `p,q`, and put

\[
t:=g(\xi)
=\frac{\lambda_1(p)}{\log p}
=\frac{\lambda_2(q)}{\log q}.
\tag{14}
\]

For all sufficiently large event coordinates, `0<t<1`. Exponentiating (14) gives the exact rational values

\[
\boxed{
 p^t=e^{\lambda_1(p)}=\frac{p+1}{p},
\qquad
 q^t=e^{\lambda_2(q)}
 =\frac{q^2+q+1}{q(q+1)}.
}
\tag{15}
\]

The number `t` is irrational. Indeed, if `t=a/b` in lowest terms and `p^{a/b}` were rational, unique factorization of rational valuations forces `b\mid a`; hence `b=1`. But an integer `t` cannot lie strictly between `0` and `1`.

Now `\log p` and `\log q` are linearly independent over `\mathbb Q`, because distinct primes are multiplicatively independent, while `1` and `t` are linearly independent over `\mathbb Q` by irrationality. The four exponentials associated with these two pairs are

\[
e^{\log p}=p,
\qquad
e^{\log q}=q,
\qquad
e^{t\log p}=p^t,
\qquad
e^{t\log q}=q^t.
\tag{16}
\]

All four are algebraic -- in fact rational by (15). Therefore (13) is an explicit counterexample to the Four Exponentials conjecture. Consequently

\[
\boxed{
\text{Four Exponentials}
\Longrightarrow
\eta_1(p)\ne\eta_2(q)
\text{ for all distinct primes }p,q.
}
\tag{17}
\]

This is the classical Alaoglu--Erdos simultaneous-jump obstruction in the present event coordinates. The corresponding **three-prime** obstruction is excluded unconditionally by the Six Exponentials theorem, which is why the classical CA transition theorem stops at a product of two distinct primes rather than allowing arbitrary collision multiplicity.

Thus the transcendence boundary is exact: `RE-102` plus the depth reduction does not leave a generic family of mysterious higher-layer ties. It leaves precisely the unresolved two-prime case at the Four-Exponentials frontier.

## 4. Conditional purity does not close the Robin argument

Assume Four Exponentials only for this paragraph. Then (17) removes every depth-two decoration from (4). Together with `RE-102`, for `Theta>Theta_*` almost every selected threshold cell on late blocks is bounded by two **simple** first-layer events

\[
\eta_1(p_-)<\eta_1(p_+),
\tag{18}
\]

where `p_-<p_+` are consecutive ordinary primes. Its open physical support chamber is exactly the first-layer image of the whole prime gap `(p_-,p_+)`.

This still does **not** make the selected fan globally first-layer-only. A selected-state switch may skip physical CA states and cross higher-layer events in its interior; exponent vectors retain all earlier prime-power increments; and the Robin height/return condition remains source-conditioned. Four Exponentials would erase the last local endpoint-tie ambiguity, but it would not supply the missing nonlocal assembly law identified by `RE-102`.

Conversely, without Four Exponentials, the binary tie channel should not be counted as another numerical exponent frontier. Its obstruction is qualitative and transcendental. Short-interval prime density can decide whether primes occur near `x(q)`; it cannot rule out the exact equality `p=x(q)` without additional arithmetic input.

## 5. Prior art and novelty boundary

Alaoglu and Erdos already identified the prime-quotient conjecture for consecutive colossally abundant numbers and its dependence on the two-prime rational-power special case of Four Exponentials. They also obtained the unconditional prime-or-product-of-two-distinct-primes theorem using the corresponding three-prime transcendence input; the later Six Exponentials theorem places that input in the standard transcendence framework. These facts are classical and are not claimed as Mathia novelty.

A targeted audit of current CA/Robin literature and standard Four/Six Exponentials references found the same classical boundary. Recent work such as Zimov's consecutive-CA analysis explicitly keeps the prime/semiprime alternative, while the current prime-layer workload framework does not remove the simultaneous-jump problem. No source located in the audit proves the Alaoglu--Erdos prime-quotient conjecture or excludes the two-prime collision unconditionally.

The durable line-specific delta is the **splice after `RE-102`**: once the selected false-RH local boundary hierarchy and the depth-at-least-three exceptional set are imposed, the entire surviving endpoint ambiguity collapses to one optional first/depth-two collision per endpoint; that collision is simultaneously an exact prime hit on the `RE-096` deformation and the classical Four-Exponentials obstruction. This separates two mechanisms that should no longer be conflated: local tie elimination is a transcendence problem, while the still-live Robin obstruction is nonlocal/source-conditioned assembly.

## 6. Falsification controls and scope

The classification (4) is an **almost-everywhere selected-threshold statement on late false-RH blocks**, not a theorem that every remote CA transition is simple or first/depth-two. The discarded threshold set may contain depth `3` or deeper boundary events, and the CA sequence globally still contains higher layers.

The semiprime theorem is used only to cap simultaneous event multiplicity. It does not imply that semiprime transitions actually occur; none is needed for the argument. Likewise (17) is conditional on the still-open Four Exponentials conjecture. Present numerical evidence for prime consecutive-CA quotients is not promoted to a theorem.

The exact-equality reduction must not be weakened to a proximity statement. The successful sparse-host estimates of `RE-095`--`RE-101` concern prime-free intervals around `x(q)` and therefore do not decide whether the real number `x(q)` itself is an integer prime. Equation (15), not a spacing estimate, is what places exact ties on the transcendence frontier.

Finally, even the conditional untied normal form leaves accumulated higher-layer history invisible to the two local endpoints. Any future contradiction must use selected-state assembly, mixed source information, or another genuinely nonlocal invariant; re-deriving first-layer endpoint timing or ordinary prime-gap geometry alone remains exhausted by `RE-083`, `RE-084`, and `RE-102`.