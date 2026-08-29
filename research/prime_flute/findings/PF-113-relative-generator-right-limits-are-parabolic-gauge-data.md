# PF-113 — relative generator right-limits are parabolic gauge data

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/BOUNDARY.

## Claim

For the canonically normalized all-composite shift clone of PF-106, the local prime/clone generator mismatch is conjugacy-invariantly summable, but its **raw matrix representation in the common global endpoint frame need not converge to the identity**. Along any subsequence on which the consecutive prime gap is a fixed value `g`, the relative generator converges to a nontrivial parabolic matrix.

This is an escaping-center effect, not an intrinsic spectral invariant. It rules out a tempting shortcut in the accepted relative-operator clue: endpoint/cross-ratio closeness and summably small local conjugacy mismatch do not justify replacing the missing common-manifold metric comparison by raw `PSL_2(R)` matrix convergence.

## 1. Exact setup

Use the zero-twist generator convention already audited in PF-099,

```text
G(a,b) = 1/(b-a) * [[a+b, -2ab], [-2, a+b]],    a<b.
```

Let

```text
V(x) = pi cot(pi/x),
x_n = V(p_n),
W(x) = V(x+1)-1,
x_n^+ = W(p_n) = x_n + d_n,
d_n = W(p_n)-V(p_n).
```

PF-106 proves `d_n>0`, decreasing, with

```text
d_n = pi^2/(3 p_n^2) + O(p_n^-3).
```

Write

```text
s_n   = x_{n+1}-x_n,
s_n^+ = x_{n+1}^+-x_n^+
      = s_n + d_{n+1}-d_n,
```

and compare corresponding generators in the fixed canonical global frame by

```text
H_n = G(x_n^+,x_{n+1}^+) G(x_n,x_{n+1})^-1.
```

The word `relative` here refers only to this marked matrix comparison. It does not assert that `H_n` is an intrinsic invariant of either quotient surface.

## 2. Exact trace identity

More generally set `b=a+s` and perturb the endpoints to `(a+alpha,b+beta)`, with

```text
s_+ = s+beta-alpha.
```

Direct `2 x 2` multiplication gives

```text
tr(H)/2 = 1 - 2 alpha beta/(s s_+),

H_21 = 2(alpha+beta)/(s s_+),

H_12 = -2/(s s_+) *
       [a^2(alpha+beta)
        + 2a alpha beta
        + 2a alpha s
        + alpha beta s
        + alpha s^2].
```

For the prime/shift-clone pair put

```text
u_n = d_n d_{n+1}/(s_n s_n^+).
```

Then

```text
tr(H_n)/2 = 1-2u_n.
```

Since `V'(x)>1` and `W'(x)=V'(x+1)>1`, both endpoint spacings dominate the corresponding ordinary prime gap. Hence `u_n -> 0`; in particular `H_n` is elliptic for all sufficiently large `n`.

If `theta_n` is the elliptic half-trace angle,

```text
cos(theta_n) = tr(H_n)/2,
```

then the exact identity becomes

```text
sin^2(theta_n/2) = u_n.
```

Because every sufficiently large prime gap is at least `2` and `d_n=O(p_n^-2)`,

```text
theta_n = O(p_n^-2),
```

so

```text
sum_n theta_n < infinity.
```

Thus the **conjugacy-invariant elliptic mismatch is summably small**.

## 3. The elliptic centers escape

The fixed point of the general relative element in the upper half-plane is

```text
z_* = -a - alpha(s+beta)/(alpha+beta)
      + i * sqrt(alpha beta (s-alpha)(s+beta))/(alpha+beta).
```

Now restrict to a subsequence with fixed consecutive prime gap

```text
p_{n+1}-p_n = g.
```

Using `a=V(p_n)~p_n`, `s_n->g`, and

```text
p_n^2 d_n       -> pi^2/3,
p_n^2 d_{n+1}   -> pi^2/3,
```

we obtain

```text
Re z_{*,n} ~ -p_n - g/2 -> -infinity,
Im z_{*,n} -> g/2.
```

The rotation angle goes to zero while the elliptic center escapes horizontally to the ideal boundary in the fixed global normalization.

## 4. Recurrent bounded gaps give parabolic matrix limits

Let

```text
c = pi^2/3.
```

Along the same fixed-gap subsequence, the exact matrix formulas above give

```text
H_11 -> 1,
H_22 -> 1,
H_21 -> 0,
H_12 -> -4c/g^2.
```

Therefore

```text
H_n -> P_g := [[1, -4 pi^2/(3g^2)], [0,1]].
```

This is a nonidentity parabolic element of `PSL_2(R)`.

The phenomenon is compatible with the previous section: small elliptic elements can converge to a nontrivial parabolic when their fixed points escape. There is no contradiction between `sum theta_n < infinity` and the nonidentity fixed-frame matrix limit.

## 5. At least one such nontrivial limit occurs unconditionally

D. H. J. Polymath proved the unconditional bounded-gap estimate

```text
H_1 = liminf_n (p_{n+1}-p_n) <= 246.
```

Reference:

- D. H. J. Polymath, *Variants of the Selberg sieve, and bounded intervals containing many primes*, Research in the Mathematical Sciences 1, Article 12 (2014), DOI `10.1186/s40687-014-0012-7`, arXiv:1407.4897.

Consequently there are infinitely many consecutive prime gaps at most `246`. Apart from the initial exceptional gap, prime gaps are even, so only finitely many values occur in that range. By pigeonhole, at least one fixed even

```text
g in {2,4,...,246}
```

occurs infinitely often. For that `g`, the canonical fixed-frame relative generators have the nontrivial parabolic subsequential limit `P_g` above.

No claim is made about which such `g` recurs, and no twin-prime input is used.

## 6. Gauge audit: the coefficient is not arithmetic spectral data

The upper-right coefficient of `P_g` is **not conjugacy invariant**. For a diagonal hyperbolic dilation

```text
D_lambda = diag(sqrt(lambda),1/sqrt(lambda)),
```

conjugation rescales a parabolic translation parameter. In particular all nonidentity parabolic elements `P_g` above lie in the same `PSL_2(R)` conjugacy class.

Therefore neither

```text
-4 pi^2/(3g^2)
```

nor the raw matrix limit itself is an intrinsic spectral invariant of the prime flute. An `n`-dependent local normalization can also move or rescale the escaping elliptic centers. The limit is meaningful only after retaining the **specific common global endpoint normalization** chosen in PF-106.

This also defeats a primality/RH interpretation of the coefficient: the comparison is against the all-composite shift clone, which preserves the same prime-gap labels, and the parameter itself is gauge-dependent.

## 7. Consequence for the relative-Laplacian clue

PF-106 through PF-111 show unusually strong local closeness of the prime flute and the all-composite shift clone: summable endpoint, shear/transverse/collar, area-weighted, canonical-separator, and pant-local marked-length defects. PF-112 separately shows that the first relative resolvent cannot be trace class under a smooth non-isometric identification.

The present calculation supplies a different boundary:

```text
summable conjugacy-invariant local generator mismatch
    does NOT imply
raw fixed-global-frame generator matrices -> identity.
```

But the converse inference is equally invalid:

```text
nontrivial raw fixed-frame parabolic right-limit
    does NOT imply
noncompact relative resolvent or spectral inequivalence.
```

The accepted clue `CLUE-affine-composite-clone-relative-operator-class.md` therefore still requires its original decisive gate: a genuine common-manifold metric comparison, or a **gauge-invariant** cross-pant/right-limit/energy obstruction. Raw representation-matrix convergence is not a substitute for either.

## 8. Novelty and prior-art audit

The ingredients themselves are classical or elementary:

- multiplication and classification of elements of `PSL_2(R)`;
- elliptic-to-parabolic degeneration when a fixed point escapes;
- unconditional bounded gaps between primes.

Targeted searches did not locate a published statement applying this fixed-frame degeneration to the exact prime-flute/all-composite shift-clone comparison. Accordingly the durable content claimed here is the **custom boundary calculation**, not a new general theorem about Fuchsian groups or bounded prime gaps.

The result is deliberately negative/boundary-level for the RH program. It removes a possible operator shortcut and identifies the exact gauge issue that any future limit-operator argument must overcome.

## 9. Falsification core

The result can be checked without any spectral assumptions:

1. multiply the two explicit generator matrices and verify `tr(H)/2 = 1-2 alpha beta/(s s_+)` and the displayed entries;
2. solve the Möbius fixed-point quadratic and verify the displayed `z_*`;
3. insert `d(p)=pi^2/(3p^2)+O(p^-3)` and a fixed prime gap `g` to obtain `P_g`;
4. independently verify the cited unconditional statement `H_1<=246` and apply the finite-pigeonhole argument.

Any failure of one of those four steps falsifies the finding. No claim about compactness, Schatten class, scattering equivalence, resonances, or RH is being smuggled into the finite calculation.
