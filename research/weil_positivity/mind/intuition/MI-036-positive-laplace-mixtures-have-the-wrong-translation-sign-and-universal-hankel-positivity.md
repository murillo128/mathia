# MI-036 — Positive Laplace mixtures have the wrong translation sign; reversing orientation makes positivity universal

**Evidence level:** exact all-order source classification from [WP-324](../../findings/WP-324-direct-laplace-translation-of-mangoldt-herglotz-source-is-strictly-sign-regular-not-polya-frequency.md), with classical Schoenberg/Karlin total-positivity ingredients. The arithmetic conclusion is a negative one: the sign mechanism is universal across positive measures.

The positive-energy Mangoldt source has the ordinary Laplace transform

`L(s)=int_0^infinity exp(-sE) dmu_+(E)`,  `s>0`.

It is tempting to feed this directly into the ordered translation geometry `K(x,y)=L(x-y)` suggested by Pólya-frequency theory. WP-324 shows that this canonical passage has the wrong sign before any arithmetic information enters. For increasing `x_1<...<x_m`, `y_1<...<y_m` with all `x_i-y_j>0`, Andréief factorization gives

`sgn det[L(x_i-y_j)] = (-1)^(m(m-1)/2)`.

The determinant is strict for the Mangoldt source because its positive measure has infinitely many support points. In particular the first nontrivial `2x2` and `3x3` ordered minors are negative. At order two this is the same fact as strict log-convexity of every nondegenerate positive-measure Laplace transform: the tilted second derivative of `log L` is a variance. `PF_2` translation positivity instead requires the opposite log-concave orientation.

This is not a prime-specific obstruction. The all-order sign law follows from the exponential kernel and positivity of the representing measure. Positive spectral reweighting preserves it whenever the transform exists. Arithmetic masses change determinant magnitudes, not their signs.

Reversing the orientation to `H(x,y)=L(x+y)` removes the alternating sign because the two exponential determinants acquire the same orientation. Every ordered Hankel minor is then positive for any positive measure with enough support points. This repairs the sign only by moving into another **universal** total-positivity class. The Lebesgue control `L(s)=1/s` already exhibits both phenomena.

The domain gate is independent and equally important. The Mangoldt source satisfies `mu_+([0,R])=R+O(1)`, hence `L(s)=1/s+O(1)` as `s downarrow 0`; its ordinary Laplace domain is exactly the positive half-line. The symmetrized source has no nonempty real bilateral-Laplace strip. Therefore the source transform is not itself the globally defined translation profile that Schoenberg's Pólya-frequency theorem assumes.

The reusable diagnostic is: **when total positivity is proposed from a positive source measure, audit determinant orientation and universality before crediting arithmetic structure.** A positive mixture can force a rigid sign pattern that is incompatible with the desired translation positivity; changing orientation can make the sign positive for reasons that erase arithmetic selectivity. A viable source-native translation route must introduce an operation whose determinant sign is not already fixed by positivity of the measure and whose domain genuinely matches the target theorem.

**Boundary.** WP-324 classifies the direct one-sided Laplace/semigroup-character construction and positive linear reweightings. It does not rule out source-forced nonlinear transforms, signed/indefinite intermediate structures, matrix/operator-valued lifts, or another canonical profile with a genuinely nonuniversal ordered-minor theorem. Those alternatives must still derive their global domain and sign from the source without importing `Xi`, its zeros, or an RH-equivalent Pólya-frequency target.
